from typing import Optional, List
from datetime import datetime


class User:
    """
    User model for MongoDB document structure
    This defines the structure of user documents in the database
    """
    
    @staticmethod
    def create_user_document(
        user_id: str,
        email: str,
        password_hash: str,
        name: str,
        role: str = "user"
    ) -> dict:
        """
        Create a new user document with default values
        
        Args:
            user_id: Unique identifier for the user
            email: User's email address
            password_hash: Hashed password
            name: User's full name
            role: User role (default: "user")
            
        Returns:
            dict: User document ready for MongoDB insertion
        """
        return {
            "_id": user_id,
            "email": email,
            "password_hash": password_hash,
            "name": name,
            "role": role,
            "is_active": True,
            "has_resume": False,
            "resume_url": None,
            "resume_filename": None,
            "resume_text": None,
            "extracted_skills": [],
            "career_role_id": None,
            "learning_time": None,
            "deadline": None,
            "education": None,
            "experience_years": None,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "last_login": datetime.utcnow()
        }
    
    @staticmethod
    def get_public_fields(user_doc: dict) -> dict:
        """
        Remove sensitive fields from user document
        
        Args:
            user_doc: User document from database
            
        Returns:
            dict: User document without sensitive data
        """
        if not user_doc:
            return None
        
        # Create a copy to avoid modifying original
        public_user = user_doc.copy()
        
        # Remove sensitive fields
        public_user.pop("password_hash", None)
        public_user.pop("resume_text", None)  # Don't expose full resume text
        
        return public_user
    
    @staticmethod
    def validate_user_role(role: str) -> bool:
        """
        Validate if the role is valid
        
        Args:
            role: Role to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        valid_roles = ["user", "admin"]
        return role in valid_roles
    
    @staticmethod
    def get_user_display_name(user_doc: dict) -> str:
        """
        Get display name for user
        
        Args:
            user_doc: User document
            
        Returns:
            str: Display name (name or email)
        """
        if not user_doc:
            return "Unknown User"
        
        return user_doc.get("name") or user_doc.get("email", "Unknown User")
