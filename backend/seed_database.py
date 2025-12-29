"""
Database Seeder Script
Run this to populate initial data for PathForge
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from app.config.settings import settings
from datetime import datetime
import uuid

async def seed_database():
    """Seed database with initial data"""
    
    # Connect to MongoDB
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client[settings.MONGODB_DB_NAME]
    
    print("🌱 Starting database seeding...")
    
    # 1. Seed Career Roles
    print("\n📚 Seeding Career Roles...")
    career_roles_collection = db["career_roles"]
    
    # Clear existing
    await career_roles_collection.delete_many({})
    
    career_roles = [
        {
            "_id": "full-stack-developer",
            "name": "Full Stack Developer",
            "description": "Build complete web applications from frontend to backend",
            "required_skills": [
                "JavaScript", "React", "Node.js", "Express", "MongoDB",
                "HTML", "CSS", "Git", "REST API", "SQL", "TypeScript"
            ],
            "difficulty": "intermediate",
            "avg_learning_time_months": 6,
            "created_at": datetime.utcnow()
        },
        {
            "_id": "data-scientist",
            "name": "Data Scientist",
            "description": "Analyze data and build machine learning models",
            "required_skills": [
                "Python", "Pandas", "NumPy", "Scikit-learn", "TensorFlow",
                "Matplotlib", "SQL", "Statistics", "Machine Learning", "Data Visualization"
            ],
            "difficulty": "advanced",
            "avg_learning_time_months": 8,
            "created_at": datetime.utcnow()
        },
        {
            "_id": "frontend-developer",
            "name": "Frontend Developer",
            "description": "Create beautiful and responsive user interfaces",
            "required_skills": [
                "HTML", "CSS", "JavaScript", "React", "Vue.js",
                "Responsive Design", "Git", "TypeScript", "Webpack", "SASS"
            ],
            "difficulty": "beginner",
            "avg_learning_time_months": 4,
            "created_at": datetime.utcnow()
        },
        {
            "_id": "backend-developer",
            "name": "Backend Developer",
            "description": "Build server-side applications and APIs",
            "required_skills": [
                "Python", "Node.js", "SQL", "MongoDB", "REST API",
                "Authentication", "Git", "Docker", "AWS", "Redis"
            ],
            "difficulty": "intermediate",
            "avg_learning_time_months": 5,
            "created_at": datetime.utcnow()
        },
        {
            "_id": "devops-engineer",
            "name": "DevOps Engineer",
            "description": "Automate and manage infrastructure and deployments",
            "required_skills": [
                "Linux", "Docker", "Kubernetes", "AWS", "CI/CD",
                "Jenkins", "Git", "Terraform", "Ansible", "Monitoring"
            ],
            "difficulty": "advanced",
            "avg_learning_time_months": 7,
            "created_at": datetime.utcnow()
        },
        {
            "_id": "mobile-developer",
            "name": "Mobile App Developer",
            "description": "Create native and cross-platform mobile applications",
            "required_skills": [
                "React Native", "JavaScript", "TypeScript", "iOS", "Android",
                "Firebase", "REST API", "Git", "Mobile UI/UX", "App Store Deployment"
            ],
            "difficulty": "intermediate",
            "avg_learning_time_months": 6,
            "created_at": datetime.utcnow()
        }
    ]
    
    result = await career_roles_collection.insert_many(career_roles)
    print(f"✅ Inserted {len(result.inserted_ids)} career roles")
    
    # 2. Create Admin User
    print("\n👤 Creating Admin User...")
    users_collection = db["users"]
    
    from app.core.security import get_password_hash
    
    admin_exists = await users_collection.find_one({"email": "admin@pathforge.com"})
    if not admin_exists:
        admin_user = {
            "_id": str(uuid.uuid4()),
            "email": "admin@pathforge.com",
            "password_hash": get_password_hash("admin123"),
            "name": "Admin User",
            "role": "admin",
            "is_active": True,
            "has_resume": False,
            "resume_url": None,
            "extracted_skills": [],
            "career_role_id": None,
            "learning_time": None,
            "deadline": None,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "last_login": None
        }
        await users_collection.insert_one(admin_user)
        print(f"✅ Admin user created: admin@pathforge.com / admin123")
    else:
        print("ℹ️ Admin user already exists")
    
    # 3. Seed Sample Resources
    print("\n📖 Seeding Sample Resources...")
    resources_collection = db["resources"]
    
    # Clear existing
    await resources_collection.delete_many({})
    
    sample_resources = [
        {
            "_id": str(uuid.uuid4()),
            "title": "JavaScript Fundamentals",
            "type": "video",
            "url": "https://www.youtube.com/watch?v=W6NZfCO5SIk",
            "description": "Learn JavaScript basics",
            "skills": ["JavaScript"],
            "difficulty": "beginner",
            "duration_minutes": 120,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "React Complete Guide",
            "type": "video",
            "url": "https://www.youtube.com/watch?v=SqcY0GlETPk",
            "description": "Complete React tutorial",
            "skills": ["React", "JavaScript"],
            "difficulty": "intermediate",
            "duration_minutes": 180,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Python for Beginners",
            "type": "article",
            "url": "https://www.python.org/about/gettingstarted/",
            "description": "Start learning Python",
            "skills": ["Python"],
            "difficulty": "beginner",
            "duration_minutes": 60,
            "created_at": datetime.utcnow()
        }
    ]
    
    result = await resources_collection.insert_many(sample_resources)
    print(f"✅ Inserted {len(result.inserted_ids)} sample resources")
    
    # 4. Create Indexes
    print("\n🔍 Creating Database Indexes...")
    
    await users_collection.create_index("email", unique=True)
    await career_roles_collection.create_index("name")
    await resources_collection.create_index("skills")
    
    print("✅ Indexes created")
    
    print("\n✨ Database seeding completed successfully!")
    print("\n📝 Summary:")
    print(f"   - Career Roles: {len(career_roles)}")
    print(f"   - Sample Resources: {len(sample_resources)}")
    print(f"   - Admin User: admin@pathforge.com / admin123")
    print(f"\n🚀 You can now start the server!")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())
