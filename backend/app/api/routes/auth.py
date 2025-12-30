from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
import uuid
import logging

from ...config.mongodb import db
from ...core.security import get_password_hash, verify_password, create_access_token
from ...core.dependencies import get_current_active_user
from ...schemas.user_schema import (
    UserSignupRequest,
    UserLoginRequest,
    TokenResponse,
    UserResponse,
    UserUpdateRequest,
    PasswordChangeRequest
)
from ...models.user import User

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/signup", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserSignupRequest):
    """
    Register a new user
    
    - **email**: Valid email address (unique)
    - **password**: Minimum 8 characters
    - **name**: User's full name
    
    Returns access token and user information
    """
    try:
        users_collection = db.get_collection("users")
        
        # Check if user already exists
        existing_user = await users_collection.find_one({"email": user_data.email})
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Create new user document
        user_id = str(uuid.uuid4())
        password_hash = get_password_hash(user_data.password)
        
        new_user = User.create_user_document(
            user_id=user_id,
            email=user_data.email,
            password_hash=password_hash,
            name=user_data.name
        )
        
        # Insert user into database
        await users_collection.insert_one(new_user)
        
        # Generate access token
        access_token = create_access_token(data={"sub": user_id})
        
        # Return response without sensitive data
        public_user = User.get_public_fields(new_user)
        
        logger.info(f"New user registered: {user_data.email}")
        
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            user=UserResponse(**public_user)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during signup: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user account"
        )


@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLoginRequest):
    """
    Login user with email and password
    
    - **email**: Registered email address
    - **password**: User's password
    
    Returns access token and user information
    """
    try:
        users_collection = db.get_collection("users")
        
        # Find user by email
        user = await users_collection.find_one({"email": credentials.email})
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        # Verify password
        if not verify_password(credentials.password, user["password_hash"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        # Check if user is active
        if not user.get("is_active", True):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive. Please contact support."
            )
        
        # Update last login timestamp
        await users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"last_login": datetime.utcnow()}}
        )
        
        # Generate access token
        access_token = create_access_token(data={"sub": user["_id"]})
        
        # Return response without sensitive data
        public_user = User.get_public_fields(user)
        
        logger.info(f"User logged in: {credentials.email}")
        
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            user=UserResponse(**public_user)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during login: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to login"
        )


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: dict = Depends(get_current_active_user)):
    """
    Get current authenticated user information
    
    Requires valid JWT token in Authorization header
    """
    try:
        public_user = User.get_public_fields(current_user)
        return UserResponse(**public_user)
    except Exception as e:
        logger.error(f"Error getting user info: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve user information"
        )


@router.put("/me", response_model=UserResponse)
async def update_user_profile(
    update_data: UserUpdateRequest,
    current_user: dict = Depends(get_current_active_user)
):
    """
    Update current user's profile
    
    - **name**: New name (optional)
    - **learning_time**: Preferred learning time (optional)
    - **deadline**: Target deadline (optional)
    """
    try:
        users_collection = db.get_collection("users")
        
        # Build update dict with only provided fields
        update_fields = {}
        if update_data.name is not None:
            update_fields["name"] = update_data.name
        if update_data.learning_time is not None:
            update_fields["learning_time"] = update_data.learning_time
        if update_data.deadline is not None:
            update_fields["deadline"] = update_data.deadline
        
        if not update_fields:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No fields to update"
            )
        
        update_fields["updated_at"] = datetime.utcnow()
        
        # Update user document
        result = await users_collection.update_one(
            {"_id": current_user["_id"]},
            {"$set": update_fields}
        )
        
        if result.modified_count == 0:
            logger.warning(f"No changes made for user {current_user['_id']}")
        
        # Fetch updated user
        updated_user = await users_collection.find_one({"_id": current_user["_id"]})
        public_user = User.get_public_fields(updated_user)
        
        logger.info(f"User profile updated: {current_user['email']}")
        
        return UserResponse(**public_user)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating user profile: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update profile"
        )


@router.post("/change-password")
async def change_password(
    password_data: PasswordChangeRequest,
    current_user: dict = Depends(get_current_active_user)
):
    """
    Change user's password
    
    - **current_password**: Current password for verification
    - **new_password**: New password (minimum 8 characters)
    """
    try:
        users_collection = db.get_collection("users")
        
        # Verify current password
        if not verify_password(password_data.current_password, current_user["password_hash"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Current password is incorrect"
            )
        
        # Check if new password is different
        if verify_password(password_data.new_password, current_user["password_hash"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New password must be different from current password"
            )
        
        # Hash new password and update
        new_password_hash = get_password_hash(password_data.new_password)
        
        await users_collection.update_one(
            {"_id": current_user["_id"]},
            {
                "$set": {
                    "password_hash": new_password_hash,
                    "updated_at": datetime.utcnow()
                }
            }
        )
        
        logger.info(f"Password changed for user: {current_user['email']}")
        
        return {"message": "Password changed successfully"}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error changing password: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to change password"
        )


@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_active_user)):
    """
    Logout user (client should remove token)
    
    Note: JWT tokens are stateless, so actual logout happens on client side
    This endpoint is provided for logging purposes
    """
    logger.info(f"User logged out: {current_user['email']}")
    return {"message": "Logged out successfully"}
