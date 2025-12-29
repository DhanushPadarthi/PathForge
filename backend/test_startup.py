"""
Test server startup and basic endpoints
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

print("✅ Testing imports...")

try:
    from app.main import app
    print("✅ FastAPI app imported successfully")
except Exception as e:
    print(f"❌ Error importing app: {e}")
    sys.exit(1)

try:
    from app.config.settings import settings
    print(f"✅ Settings loaded: {settings.APP_NAME}")
    print(f"   MongoDB: {settings.MONGODB_URI}")
    print(f"   OpenAI: {'*' * 20 + settings.OPENAI_API_KEY[-10:]}")
except Exception as e:
    print(f"❌ Error loading settings: {e}")
    sys.exit(1)

print("\n🎯 Available routes:")
for route in app.routes:
    if hasattr(route, 'path') and hasattr(route, 'methods'):
        methods = ','.join(route.methods) if route.methods else 'N/A'
        print(f"   {methods:10} {route.path}")

print("\n✅ All basic checks passed!")
print("\n🚀 To start the server, run:")
print("   cd backend")
print("   uvicorn app.main:app --reload")
