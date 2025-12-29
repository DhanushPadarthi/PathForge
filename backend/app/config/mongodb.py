from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from .settings import settings
import logging

logger = logging.getLogger(__name__)

class MongoDB:
    client: Optional[AsyncIOMotorClient]
    
    def __init__(self):
        self.client = None
    
    @classmethod
    async def connect_db(cls):
        """Connect to MongoDB"""
        try:
            cls.client = AsyncIOMotorClient(settings.MONGODB_URI)
            # Test connection
            await cls.client.admin.command('ping')
            logger.info(f"✅ Connected to MongoDB: {settings.MONGODB_DB_NAME}")
        except Exception as e:
            logger.error(f"❌ MongoDB connection failed: {e}")
            raise
    
    @classmethod
    async def close_db(cls):
        """Close MongoDB connection"""
        if cls.client:
            cls.client.close()
            logger.info("MongoDB connection closed")
    
    @classmethod
    def get_db(cls):
        """Get database instance"""
        if not cls.client:
            raise Exception("Database not connected. Call connect_db() first.")
        return cls.client[settings.MONGODB_DB_NAME]
    
    @classmethod
    def get_collection(cls, collection_name: str):
        """Get collection from database"""
        db = cls.get_db()
        return db[collection_name]

# Database instance
db = MongoDB()
