# PathForge - Team File Assignments

## AWS Mini Hackathon Team Structure

### Team Members & Branches
- **Dhanush** - Backend Team Lead - Branch: `dhanush`
- **Varun** - Backend Team - Branch: `varun`
- **Varsha** - Backend Team - Branch: `varsha`
- **Mrinaliny** - Backend Team - Branch: `mrinaliny`
- **Varshareddy** - Presentation & Documentation - Branch: `varshareddy`

---

## Development Strategy

### Phase 1: Backend Development (CURRENT PRIORITY)
**All team members focus on backend first - Complete backend before moving to frontend**

### 🔧 Backend Team
**Members:** Dhanush (Lead), Varun, Varsha, Mrinaliny

**Focus:** Build and complete all API endpoints, database models, AI integrations, and business logic

### 🎯 Presentation & Documentation
**Member:** Varshareddy

**Focus:** Create presentation deck, polish documentation, prepare demo materials

---

## File Assignments

### 🔧 Dhanush (Backend Lead) - Core Backend & Resume Processing
**Branch:** `dhanush`  
**Team:** Backend

#### Your Files:
- `backend/main.py` - FastAPI application setup and configuration
- `backend/database.py` - MongoDB connection and database setup
- `backend/models.py` - Database models and schemas (User, Roadmap, Progress, etc.)
- `backend/routes/resume.py` - Resume upload and analysis endpoints
- `backend/services/resume_parser.py` - Resume text extraction (PDF/DOCX parsing)

#### Key Responsibilities:
- FastAPI application setup and middleware configuration
- MongoDB database connection and initialization
- Database schema design and models
- Resume upload endpoint (handle PDF/DOCX files)
- Resume text extraction using PyPDF2 and python-docx
- Firebase Storage integration for file uploads
- Error handling and validation
- Integration of all routes and services
- Final code review and merging

#### Features to Implement:
- ✅ FastAPI app with CORS middleware
- ✅ MongoDB connection with error handling
- ✅ User, Roadmap, Resource, Progress models
- ✅ Resume upload endpoint (POST /api/resume/upload)
- ✅ PDF and DOCX text extraction
- ✅ File validation and security checks
- ✅ Firebase Storage file upload
- ✅ Resume data storage in MongoDB

#### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout dhanush

# Set up Python environment
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Daily workflow
git checkout dhanush
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented resume upload and parsing"
git push origin dhanush

# When merging all branches to main
git checkout main
git pull origin main
git merge dhanush
git merge varun
git merge varsha
git merge mrinaliny
git push origin main
```

---

### 🔧 Varun - AI Integration & Roadmap Generation
**Branch:** `varun`  
**Team:** Backend

#### Your Files:
- `backend/routes/roadmap.py` - Roadmap generation and retrieval endpoints
- `backend/routes/resources.py` - Learning resources management endpoints
- `backend/routes/admin.py` - Admin panel endpoints
- `backend/services/chatgpt_service.py` - OpenAI/ChatGPT API integration
- `backend/services/roadmap_service.py` - Roadmap generation business logic
- `backend/requirements.txt` - Python dependencies

#### Key Responsibilities:
- ChatGPT API integration for AI features
- AI-powered skill extraction from resume
- Skill gap analysis using AI
- Deadline-based roadmap generation
- Resource recommendation algorithm
- Admin CRUD operations
- Module summary generation
- Sequential resource unlocking logic

#### Features to Implement:
- ✅ ChatGPT service for skill extraction
- ✅ Skill gap analysis (compare current vs required skills)
- ✅ Roadmap generation endpoint (POST /api/roadmap/generate)
- ✅ Time-based roadmap alignment (30min/1hr/2hr daily)
- ✅ Resource recommendation API (GET /api/resources)
- ✅ Sequential unlocking mechanism
- ✅ Module summary generation
- ✅ Admin endpoints (POST/PUT/DELETE for roles & resources)
- ✅ All Python dependencies in requirements.txt

#### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout varun

# Set up Python environment
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Daily workflow
git checkout varun
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented AI roadmap generation with ChatGPT"
git push origin varun
```

---

### 🔧 Varsha - Authentication & User Management
**Branch:** `varsha`  
**Team:** Backend

#### Your Files:
- `backend/routes/auth.py` - Authentication endpoints (Email/Google OAuth)
- `backend/routes/user.py` - User profile management endpoints
- `backend/services/auth_service.py` - Firebase authentication logic
- `backend/services/user_service.py` - User management business logic
- `backend/middleware/auth_middleware.py` - Authentication middleware

#### Key Responsibilities:
- User authentication endpoints (Email & Google)
- Firebase Authentication backend integration
- JWT token validation
- User profile CRUD operations
- User session management
- Protected route middleware
- User data validation
- Password hashing and security

#### Features to Implement:
- ✅ User signup endpoint (POST /api/auth/signup)
- ✅ User login endpoint (POST /api/auth/login)
- ✅ Google OAuth integration (POST /api/auth/google)
- ✅ JWT token generation and validation
- ✅ User profile creation (POST /api/user/profile)
- ✅ User profile retrieval (GET /api/user/profile)
- ✅ User profile update (PUT /api/user/profile)
- ✅ Authentication middleware for protected routes
- ✅ User session handling
- ✅ Basic questionnaire endpoint for users without resume

#### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout varsha

# Set up Python environment
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Daily workflow
git checkout varsha
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented authentication with Firebase and JWT"
git push origin varsha
```

---

### 🔧 Mrinaliny - Progress Tracking & Analytics
**Branch:** `mrinaliny`  
**Team:** Backend

#### Your Files:
- `backend/routes/progress.py` - Progress tracking endpoints
- `backend/routes/analytics.py` - User analytics and statistics endpoints
- `backend/services/progress_service.py` - Progress calculation and tracking logic
- `backend/services/analytics_service.py` - Analytics aggregation logic
- `backend/utils/helpers.py` - Helper functions and utilities

#### Key Responsibilities:
- Progress tracking system
- Complete/Skip resource functionality
- Progress percentage calculation
- Real-time progress updates
- Module completion tracking
- User learning statistics
- Time tracking for resources
- Admin analytics dashboard data
- Database query optimization

#### Features to Implement:
- ✅ Mark resource as complete (POST /api/progress/complete)
- ✅ Skip resource endpoint (POST /api/progress/skip)
- ✅ Get user progress (GET /api/progress)
- ✅ Progress percentage calculation
- ✅ Module completion status
- ✅ Learning time tracking
- ✅ Progress history retrieval
- ✅ User statistics (GET /api/analytics/user/:id)
- ✅ Admin analytics (GET /api/analytics/admin)
- ✅ Helper utilities (date formatting, calculations, etc.)

#### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout mrinaliny

# Set up Python environment
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Daily workflow
git checkout mrinaliny
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented progress tracking and analytics"
git push origin mrinaliny
```

---

### 🎯 Varshareddy - Presentation & Documentation
**Branch:** `varshareddy`  
**Team:** Presentation

#### Your Files:
- `PRD.md` - Product Requirements Document (already updated)
- `README.md` - Project documentation (already updated)
- `PRESENTATION.pptx` or `PRESENTATION.pdf` - Demo presentation deck

#### Key Responsibilities:
- Create compelling presentation for hackathon demo
- Design presentation slides with:
  - Problem statement
  - Solution overview
  - Key features demonstration
  - Technology stack
  - Architecture diagram
  - User flow walkthrough
  - Future enhancements
  - Team introduction
- Polish existing documentation
- Create demo script
- Prepare talking points for presentation
- Design visual assets (optional)

#### Presentation Structure:
1. **Title Slide** - PathForge branding
2. **Problem Statement** - Why PathForge is needed
3. **Solution Overview** - What PathForge does
4. **Target Users** - Who benefits
5. **Key Features** - 8 core features with icons
6. **Dual Entry Flow** - With/Without resume paths
7. **Technology Stack** - Show tech logos
8. **System Architecture** - Backend + Frontend + AI diagram
9. **User Journey** - Step-by-step flow
10. **Demo Screenshots** - UI mockups or actual screens
11. **Future Enhancements** - AI Mentor, Project Generator, Trending Skills
12. **Team** - Team member roles
13. **Thank You** - Contact & GitHub link

#### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout varshareddy

# Daily workflow
git checkout varshareddy
git pull origin main
# ... work on presentation and docs ...
git add .
git commit -m "Created presentation deck for demo"
git push origin varshareddy
```

---

## Backend Development Checklist

### Phase 1 Tasks (Backend Priority)

#### Core Infrastructure (Dhanush)
- [ ] FastAPI app setup with CORS
- [ ] MongoDB connection
- [ ] Database models (User, Roadmap, Resource, Progress)
- [ ] Resume upload endpoint
- [ ] PDF/DOCX text extraction
- [ ] Firebase Storage integration

#### AI & Roadmap (Varun)
- [ ] ChatGPT service setup
- [ ] AI skill extraction
- [ ] Skill gap analysis
- [ ] Roadmap generation algorithm
- [ ] Resource recommendation system
- [ ] Admin CRUD endpoints
- [ ] requirements.txt with all dependencies

#### Authentication (Varsha)
- [ ] User signup/login endpoints
- [ ] Firebase Authentication integration
- [ ] Google OAuth
- [ ] JWT token handling
- [ ] Auth middleware
- [ ] User profile CRUD

#### Progress & Analytics (Mrinaliny)
- [ ] Progress tracking endpoints
- [ ] Complete/Skip functionality
- [ ] Progress percentage calculation
- [ ] Analytics endpoints
- [ ] Time tracking
- [ ] Helper utilities

---

## Backend Dependencies (requirements.txt)

```txt
fastapi==0.104.1
uvicorn==0.24.0
pymongo==4.6.0
python-dotenv==1.0.0
openai==1.3.7
python-multipart==0.0.6
PyPDF2==3.0.1
python-docx==1.1.0
firebase-admin==6.3.0
pyjwt==2.8.0
passlib==1.7.4
bcrypt==4.1.1
python-jose==3.3.0
```

---

## Environment Variables (.env file)

```bash
# MongoDB
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/pathforge

# OpenAI
OPENAI_API_KEY=sk-...

# Firebase
FIREBASE_TYPE=service_account
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_PRIVATE_KEY_ID=...
FIREBASE_PRIVATE_KEY=...
FIREBASE_CLIENT_EMAIL=...
FIREBASE_CLIENT_ID=...
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token

# JWT
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
```

---

## Quick Git Workflow Reference

### Daily Workflow for Everyone

```bash
# 1. Start your day
git checkout <your-branch>
git pull origin main

# 2. Work on your assigned files
# ... code, test, debug ...

# 3. Check what you changed
git status

# 4. Stage your changes
git add .

# 5. Commit with descriptive message
git commit -m "Implemented [feature name]"

# 6. Push to your branch
git push origin <your-branch>
```

### Common Git Commands

| Command | Purpose |
|---------|---------|
| `git status` | See modified files |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit with message |
| `git push origin <branch>` | Push to your branch |
| `git pull origin main` | Get latest from main |
| `git checkout <branch>` | Switch branches |
| `git log --oneline` | View commit history |

---

## Backend Setup Instructions

### Prerequisites
- Python 3.9+
- MongoDB Atlas account
- OpenAI API key
- Firebase project

### Setup Steps

1. **Clone Repository**
```bash
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
```

2. **Switch to Your Branch**
```bash
git checkout <your-branch-name>
```

3. **Set Up Python Environment**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

5. **Create .env File**
```bash
# Create .env in backend/ directory
# Add all environment variables listed above
```

6. **Run Backend Server**
```bash
uvicorn main:app --reload
```

Server will run at: `http://localhost:8000`

---

## API Endpoints Overview

### Authentication (Varsha)
- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/google` - Google OAuth login
- `GET /api/auth/verify` - Verify JWT token

### User (Varsha)
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update user profile
- `POST /api/user/questionnaire` - Submit questionnaire (no resume flow)

### Resume (Dhanush)
- `POST /api/resume/upload` - Upload and parse resume
- `GET /api/resume/:userId` - Get parsed resume data

### Roadmap (Varun)
- `POST /api/roadmap/generate` - Generate personalized roadmap
- `GET /api/roadmap/:userId` - Get user's roadmap
- `PUT /api/roadmap/:id` - Update roadmap

### Resources (Varun)
- `GET /api/resources/:roadmapId` - Get resources for roadmap
- `GET /api/resources/:id/next` - Get next unlocked resource

### Progress (Mrinaliny)
- `POST /api/progress/complete` - Mark resource complete
- `POST /api/progress/skip` - Skip resource
- `GET /api/progress/:userId` - Get user progress

### Analytics (Mrinaliny)
- `GET /api/analytics/user/:userId` - User statistics
- `GET /api/analytics/admin` - Admin dashboard data

### Admin (Varun)
- `POST /api/admin/roles` - Add career role
- `PUT /api/admin/roles/:id` - Update career role
- `DELETE /api/admin/roles/:id` - Delete career role
- `POST /api/admin/resources` - Add learning resource
- `PUT /api/admin/resources/:id` - Update learning resource

---

## Testing Your Backend

### Using Postman/Thunder Client

1. **Test Authentication**
```json
POST http://localhost:8000/api/auth/signup
{
  "email": "test@example.com",
  "password": "password123",
  "name": "Test User"
}
```

2. **Test Resume Upload**
```
POST http://localhost:8000/api/resume/upload
Headers: Authorization: Bearer <token>
Body: form-data
- file: <select PDF/DOCX>
```

3. **Test Roadmap Generation**
```json
POST http://localhost:8000/api/roadmap/generate
Headers: Authorization: Bearer <token>
{
  "careerGoal": "Full Stack Developer",
  "learningTime": "1hr"
}
```

---

## Communication & Collaboration

### Daily Standup (Recommended)
- What did you complete yesterday?
- What will you work on today?
- Any blockers?

### Code Review Process
1. Push to your branch
2. Create Pull Request (optional)
3. Tag Dhanush for review
4. Dhanush merges to main

### Naming Conventions
- **Files**: lowercase with underscores (`resume_parser.py`)
- **Functions**: snake_case (`extract_resume_text()`)
- **Classes**: PascalCase (`UserModel`)
- **Constants**: UPPER_SNAKE_CASE (`JWT_SECRET_KEY`)
- **Endpoints**: kebab-case (`/api/resume/upload`)

---

## Important Guidelines

### ⚠️ DO NOT:
- Push directly to `main` branch
- Modify files not assigned to you
- Commit without testing
- Share API keys in code (use .env)
- Delete others' work

### ✅ DO:
- Work only on your assigned files
- Pull from main regularly
- Test before committing
- Write clear commit messages
- Ask for help when stuck
- Document your code
- Handle errors properly

---

## Troubleshooting

### Python Environment Issues
```bash
# If venv doesn't activate
python -m venv venv --clear
venv\Scripts\activate
```

### MongoDB Connection Failed
- Check MONGODB_URI in .env
- Verify IP whitelist in MongoDB Atlas
- Test connection string

### Git Merge Conflicts
```bash
# Update from main first
git pull origin main
# Resolve conflicts in files
git add .
git commit -m "Resolved merge conflicts"
git push origin <your-branch>
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

---

## GitHub Repository
**URL:** https://github.com/DhanushPadarthi/PathForge.git

## Branch Structure
- `main` - Production code (Dhanush merges here)
- `dhanush` - Core backend & resume processing
- `varun` - AI integration & roadmap
- `varsha` - Authentication & user management
- `mrinaliny` - Progress tracking & analytics
- `varshareddy` - Presentation & documentation

---

## Timeline Suggestion

### Day 1
- **All**: Setup repository, environment, .env files
- **Dhanush**: FastAPI setup, MongoDB connection, models
- **Varun**: ChatGPT service setup, requirements.txt
- **Varsha**: Auth endpoints structure
- **Mrinaliny**: Progress endpoints structure

### Day 2
- **Dhanush**: Resume upload and parsing
- **Varun**: Skill extraction and gap analysis
- **Varsha**: Complete authentication flow
- **Mrinaliny**: Progress tracking logic

### Day 3
- **Dhanush**: Complete resume features
- **Varun**: Roadmap generation algorithm
- **Varsha**: User profile CRUD
- **Mrinaliny**: Analytics endpoints

### Day 4
- **All**: Testing, bug fixes, integration
- **Varun**: Admin endpoints
- **Dhanush**: Merge all branches

### Day 5
- **All**: Final testing and deployment
- **Varshareddy**: Final presentation ready

---

**Focus on Backend First - Build Solid API Foundation! 🚀**
