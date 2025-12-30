import firebase_admin
from firebase_admin import credentials, auth, storage
from .settings import settings
import logging
import os

logger = logging.getLogger(__name__)

class FirebaseConfig:
    _initialized = False
    
    @classmethod
    def initialize(cls):
        """Initialize Firebase Admin SDK"""
        if cls._initialized:
            return
        
        try:
            # Initialize with credentials file if provided
            if settings.FIREBASE_CREDENTIALS_PATH and os.path.exists(settings.FIREBASE_CREDENTIALS_PATH):
                cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
                firebase_admin.initialize_app(cred, {
                    'storageBucket': settings.FIREBASE_STORAGE_BUCKET
                })
            else:
                # Initialize with default credentials (for development)
                firebase_admin.initialize_app()
            
            cls._initialized = True
            logger.info("✅ Firebase Admin SDK initialized")
        except Exception as e:
            logger.warning(f"⚠️ Firebase initialization failed: {e}")
            logger.info("Continuing without Firebase (auth will use JWT only)")
    
    @classmethod
    def verify_token(cls, token: str):
        """Verify Firebase ID token"""
        try:
            decoded_token = auth.verify_id_token(token)
            return decoded_token
        except Exception as e:
            logger.error(f"Token verification failed: {e}")
            return None
    
    @classmethod
    def get_storage_bucket(cls):
        """Get Firebase Storage bucket"""
        if not cls._initialized:
            raise Exception("Firebase not initialized")
        return storage.bucket()

# Initialize Firebase on module import
firebase_config = FirebaseConfig()
