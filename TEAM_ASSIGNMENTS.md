# PathForge - Backend Team File Assignments

## ✅ Complete Project Structure Created

All placeholder files have been created. Each team member must implement the logic in their assigned files.

---

## 👥 Team Members & Branches

| Member | Role | Branch | Focus Area |
|--------|------|--------|------------|
| **Dhanush** | Backend Lead | `dhanush` | Core Setup & Authentication |
| **Varun** | Backend Developer | `varun` | Resume & Skill Analysis |
| **Varsha** | Backend Developer | `varsha` | AI & Roadmap Generation |
| **Mrinaliny** | Backend Developer | `mrinaliny` | Resources & Progress Tracking |
| **Varshareddy** | Documentation Lead | `varshareddy` | Presentation & PPT |

---

## 🔧 Backend File Assignments

### 1️⃣ Dhanush - Core Backend & Authentication System
**Branch:** `dhanush`  
**Role:** Backend Team Lead

#### 📂 Your Files (9 files):

**Application Setup:**
- ✅ `backend/app/main.py` - FastAPI app initialization, CORS, middleware, router registration
- ✅ `backend/app/config/settings.py` - Environment variables, app settings, configuration management
- ✅ `backend/app/config/mongodb.py` - MongoDB Atlas connection, database initialization
- ✅ `backend/app/config/firebase.py` - Firebase Admin SDK setup for auth & storage

**Security & Authentication:**
- ✅ `backend/app/core/security.py` - Password hashing (bcrypt), JWT token creation/validation
- ✅ `backend/app/core/dependencies.py` - FastAPI dependencies (get_current_user, get_db, admin_required)

**Authentication Routes:**
- ✅ `backend/app/api/routes/auth.py` - Login, Register, Google OAuth, Logout, Get Current User

**Models & Schemas:**
- ✅ `backend/app/models/user.py` - User database model (fields: id, email, password_hash, role, etc.)
- ✅ `backend/app/schemas/user_schema.py` - Pydantic schemas (UserCreate, UserLogin, UserResponse)

#### 🎯 Key Responsibilities:
1. Setup FastAPI application with CORS middleware
2. Configure MongoDB connection (use Motor for async operations)
3. Configure Firebase Admin SDK
4. Implement password hashing using bcrypt
5. Create JWT token generation and validation
6. Build authentication endpoints (register, login, Google OAuth)
7. Create authentication dependencies for protected routes
8. Implement role-based access control (Student/Admin)

#### 📚 Libraries to Use:
- `fastapi`, `uvicorn`
- `motor` (async MongoDB)
- `firebase-admin`
- `passlib[bcrypt]` (password hashing)
- `python-jose` (JWT tokens)

---

### 2️⃣ Varun - Resume Processing & Skill Analysis
**Branch:** `varun`  
**Role:** Backend Developer

#### 📂 Your Files (6 files):

**API Routes:**
- ✅ `backend/app/api/routes/resume.py` - Upload resume, Parse resume, Get resume data, Delete resume
- ✅ `backend/app/api/routes/skill_analysis.py` - Analyze skills, Gap analysis, Get required skills, Process questionnaire

**Services:**
- ✅ `backend/app/services/resume_parser.py` - Extract text from PDF/DOCX, Parse resume sections
- ✅ `backend/app/services/skill_analyzer.py` - Compare skills, Identify gaps, Calculate proficiency

**Models & Utils:**
- ✅ `backend/app/models/skill.py` - Skill model (name, category, proficiency_level, source)
- ✅ `backend/app/utils/validators.py` - File validation (PDF/DOCX), Email validation, Input sanitization

#### 🎯 Key Responsibilities:
1. Implement resume file upload (PDF/DOCX) with Firebase Storage
2. Extract text from PDF using PyPDF2 or pdfplumber
3. Extract text from DOCX using python-docx
4. Parse resume sections (education, experience, skills, projects)
5. Create questionnaire for users without resume
6. Compare user skills with required role skills
7. Identify skill gaps and missing competencies
8. Calculate skill proficiency levels
9. Validate file types and sizes

#### 📚 Libraries to Use:
- `PyPDF2` or `pdfplumber` (PDF parsing)
- `python-docx` (DOCX parsing)
- `firebase-admin` (file storage)
- `python-multipart` (file uploads)

---

### 3️⃣ Varsha - AI Integration & Roadmap Generation
**Branch:** `varsha`  
**Role:** Backend Developer

#### 📂 Your Files (6 files):

**AI Services:**
- ✅ `backend/app/services/ai_service.py` - OpenAI/ChatGPT integration for all AI operations
- ✅ `backend/app/services/roadmap_generator.py` - Generate personalized roadmaps, Create modules, Calculate deadlines

**API Routes:**
- ✅ `backend/app/api/routes/roadmap.py` - Generate roadmap, Get roadmap, Update roadmap, Delete roadmap, Get modules

**Models & Schemas:**
- ✅ `backend/app/models/roadmap.py` - Roadmap model (user_id, career_role_id, modules, deadline, status)
- ✅ `backend/app/models/career_role.py` - Career role model (name, description, required_skills)
- ✅ `backend/app/schemas/roadmap_schema.py` - Pydantic schemas (RoadmapCreate, RoadmapResponse, ModuleSchema)

#### 🎯 Key Responsibilities:
1. Integrate OpenAI/ChatGPT API for AI operations
2. Create prompts for skill extraction from resume
3. Create prompts for skill gap analysis
4. Generate personalized learning roadmaps based on:
   - User's current skills
   - Target career role
   - Available learning time
   - Deadline
5. Structure roadmap into sequential modules
6. Create milestones and checkpoints
7. Implement roadmap CRUD operations
8. Handle AI API errors gracefully

#### 📚 Libraries to Use:
- `openai` (ChatGPT API)
- `pydantic` (data validation)

---

### 4️⃣ Mrinaliny - Resources, Progress & Admin Panel
**Branch:** `mrinaliny`  
**Role:** Backend Developer

#### 📂 Your Files (10 files):

**API Routes:**
- ✅ `backend/app/api/routes/resources.py` - Get resources, Recommend resources, Get resources by module
- ✅ `backend/app/api/routes/progress.py` - Complete resource, Skip resource, Get progress, Get summary, Update progress
- ✅ `backend/app/api/routes/admin.py` - User management, Career role management, Resource management, Statistics

**Services:**
- ✅ `backend/app/services/resource_recommender.py` - AI-powered resource recommendations
- ✅ `backend/app/services/progress_tracker.py` - Track progress, Calculate completion %, Generate summaries

**Models & Schemas:**
- ✅ `backend/app/models/resource.py` - Resource model (title, url, type, estimated_time, difficulty, tags)
- ✅ `backend/app/models/progress.py` - Progress model (user_id, resource_id, status, time_spent)
- ✅ `backend/app/schemas/resource_schema.py` - Resource schemas
- ✅ `backend/app/schemas/progress_schema.py` - Progress schemas

**Utils:**
- ✅ `backend/app/utils/helpers.py` - Date/time utilities, File handling, Response formatting, Error handling

#### 🎯 Key Responsibilities:
1. **Resource Recommendation:**
   - Use AI to recommend learning resources
   - Filter resources by skill, difficulty, time
   - Match resources to roadmap modules
   - Curate external learning links (YouTube, courses, articles)

2. **Progress Tracking:**
   - Track user progress through roadmap
   - Handle complete/skip resource actions
   - Calculate completion percentages
   - Track time spent on learning
   - Generate module completion summaries

3. **Admin Panel:**
   - User management (view, delete users)
   - Career role CRUD operations
   - Learning resource CRUD operations
   - Platform statistics (user count, completion rates)
   - Admin authorization checks

4. **Utilities:**
   - Date/time helper functions
   - File upload handling
   - Response formatting
   - Error handling utilities

#### 📚 Libraries to Use:
- `openai` (for resource recommendations)
- `datetime` (time tracking)
- `pymongo` (database queries)

---

### 5️⃣ Varshareddy - Presentation & Documentation
**Branch:** `varshareddy`  
**Role:** Documentation & Presentation Lead

#### 📂 Your Responsibilities:

**Presentation (PPT):**
- ✅ Create comprehensive PowerPoint presentation
- ✅ Slides on problem statement and solution
- ✅ System architecture diagram
- ✅ User flow diagrams
- ✅ Technology stack overview
- ✅ Feature demonstrations
- ✅ Future scope and roadmap
- ✅ Team introduction slide

**Documentation:**
- ✅ Polish README.md files
- ✅ Update PRD.md if needed
- ✅ Create API documentation
- ✅ Write setup instructions
- ✅ Create demo script
- ✅ Prepare Q&A for judges

**Demo Preparation:**
- ✅ Test complete application flow
- ✅ Prepare sample resumes for demo
- ✅ Create demo user accounts
- ✅ Record demo video (optional)
- ✅ Prepare talking points

#### 🎯 Key Deliverables:
1. Professional PowerPoint presentation (15-20 slides)
2. Updated documentation files
3. API documentation
4. Demo script and talking points
5. Sample data for demonstration

---

## 📋 Development Workflow

### Step 1: Clone Repository & Setup Branch (Day 1)

**Repository URL:** `https://github.com/DhanushPadarthi/PathForge.git`

#### For All Team Members:

```bash
# 1. Clone the repository
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge

# 2. Switch to YOUR branch (already created)
git checkout <your-branch-name>
# Example: git checkout dhanush
# Example: git checkout varun
# Example: git checkout varsha
# Example: git checkout mrinaliny
# Example: git checkout varshareddy

# 3. Verify you're on the correct branch
git branch
# You should see * next to your branch name

# 4. Setup Python virtual environment (Backend members only)
cd backend
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Setup environment variables
copy .env.example .env          # Windows
# or
cp .env.example .env            # Mac/Linux

# 7. Edit .env file with your credentials
# Add MongoDB URI, Firebase credentials, OpenAI API key, etc.
```

---

### Step 2: Daily Development Workflow (Day 1-3)

#### Before Starting Work Each Day:

```bash
# 1. Switch to your branch
git checkout <your-branch-name>

# 2. Pull latest changes from main
git pull origin main

# 3. Check status
git status
```

#### While Working:

1. **Open your assigned files** (check TEAM_ASSIGNMENTS.md for your file list)
2. **Read the comments** in each file explaining what to implement
3. **Implement functionality** step by step
4. **Test your code** frequently
   - For API endpoints: Use Postman or Thunder Client
   - For functions: Write test cases or manual testing

#### After Completing a Feature:

```bash
# 1. Check what files you've modified
git status

# 2. Stage your changes
git add .
# Or add specific files:
git add backend/app/api/routes/auth.py

# 3. Commit with a clear message
git commit -m "Implemented user login endpoint with JWT authentication"
# More examples:
# git commit -m "Added resume PDF parser using PyPDF2"
# git commit -m "Created roadmap generation with ChatGPT integration"
# git commit -m "Implemented progress tracking endpoints"

# 4. Push to YOUR branch on GitHub
git push origin <your-branch-name>
# Example: git push origin dhanush
# Example: git push origin varun
```

#### Commit Message Guidelines:

✅ **Good commit messages:**
- `"Implemented JWT token generation and validation"`
- `"Added MongoDB connection with Motor async driver"`
- `"Created resume upload endpoint with Firebase Storage"`
- `"Fixed bug in skill gap analysis algorithm"`

❌ **Bad commit messages:**
- `"Updated files"`
- `"Changes"`
- `"Fix"`

---

### Step 3: Integration & Merge (Day 4)

#### Creating a Pull Request:

```bash
# 1. Make sure all your work is committed and pushed
git status
git push origin <your-branch-name>

# 2. Go to GitHub repository
# https://github.com/DhanushPadarthi/PathForge

# 3. Click "Pull Requests" tab

# 4. Click "New Pull Request"

# 5. Select:
#    - Base: main
#    - Compare: <your-branch-name>

# 6. Add title and description:
#    Title: "Backend: Authentication System Implementation"
#    Description: List what you've implemented

# 7. Request review from Dhanush (team lead)

# 8. Wait for approval and merge
```

#### After Your PR is Merged:

```bash
# Update your local main branch
git checkout main
git pull origin main

# Update your branch with latest main
git checkout <your-branch-name>
git merge main

# Continue working on new features
```

---

### Step 4: Testing & Polish (Day 5)

```bash
# 1. Pull latest integrated code
git checkout main
git pull origin main

# 2. Test the complete application
cd backend
uvicorn app.main:app --reload

# 3. Run tests (if available)
pytest

# 4. Fix any bugs found
git checkout <your-branch-name>
# Fix bugs in your files
git add .
git commit -m "Fixed bug in authentication middleware"
git push origin <your-branch-name>

# 5. Create final PR if needed
```

---

### 🔄 Common Git Commands Reference

```bash
# Check which branch you're on
git branch

# See all branches (local and remote)
git branch -a

# Switch between branches
git checkout <branch-name>

# See what files you've changed
git status

# See what changes you've made
git diff

# Undo changes to a file (before commit)
git checkout -- <filename>

# View commit history
git log --oneline

# Pull latest changes from main to your branch
git checkout <your-branch-name>
git pull origin main

# Stash changes temporarily
git stash
git stash pop

# Discard all local changes (CAREFUL!)
git reset --hard HEAD
```

---

### ⚠️ Important Git Rules

**DO:**
- ✅ Always work on YOUR branch
- ✅ Commit frequently with clear messages
- ✅ Push to YOUR branch regularly
- ✅ Pull from main before starting work
- ✅ Test before committing

**DON'T:**
- ❌ Never push directly to `main` branch
- ❌ Never work on someone else's branch
- ❌ Never commit sensitive data (.env files)
- ❌ Never force push (`git push -f`)
- ❌ Never commit without testing

---

### 🆘 Git Troubleshooting

#### "I'm on the wrong branch!"
```bash
git stash                    # Save your changes
git checkout <correct-branch>
git stash pop               # Apply your changes
```

#### "I need to update my branch with latest main"
```bash
git checkout <your-branch>
git pull origin main
# If conflicts, resolve them in your code editor
git add .
git commit -m "Merged latest changes from main"
git push origin <your-branch>
```

#### "I committed to the wrong branch!"
```bash
git log                     # Copy the commit hash
git checkout <correct-branch>
git cherry-pick <commit-hash>
git push origin <correct-branch>
```

#### "I want to undo my last commit"
```bash
# Keep the changes but undo commit
git reset --soft HEAD~1

# Discard the changes and commit
git reset --hard HEAD~1
```

---

## 🔗 Integration Points

**Critical Dependencies:**

1. **Dhanush → Everyone:**
   - Database connection must work first
   - Authentication system needed for all protected routes
   - Models must be defined before other routes use them

2. **Varun → Varsha:**
   - Skill analysis output feeds into roadmap generation
   - Resume parsing data used by AI service

3. **Varsha → Mrinaliny:**
   - Roadmap structure needed for resource recommendation
   - AI service used for resource recommendations

4. **All → Varshareddy:**
   - Working features needed for demo
   - Documentation inputs from all members

---

## ✅ Success Criteria

### For Each Backend Member:
- [ ] All assigned files implemented
- [ ] Code follows Python/FastAPI best practices
- [ ] All endpoints tested with Postman/Thunder Client
- [ ] Error handling implemented
- [ ] Code committed to branch
- [ ] Pull Request created

### For Varshareddy:
- [ ] Presentation deck completed
- [ ] Documentation polished
- [ ] Demo script prepared
- [ ] Sample data ready

---

## 🆘 Need Help?

**Common Issues:**

1. **MongoDB Connection Issues:**
   - Check MONGODB_URI in .env
   - Verify network access in MongoDB Atlas
   - Ask Dhanush for help

2. **Firebase Issues:**
   - Verify Firebase credentials in .env
   - Check Firebase console settings
   - Ask Dhanush for help

3. **OpenAI API Issues:**
   - Verify API key is valid
   - Check API quota/limits
   - Ask Varsha for help

4. **File Parsing Issues:**
   - Test with different PDF/DOCX formats
   - Check file encoding
   - Ask Varun for help

**Communication:**
- Report blockers immediately in team chat
- Daily standup updates on progress
- Help each other when stuck

---

## 🎯 Timeline (5 Days)

| Day | Focus | Deliverable |
|-----|-------|-------------|
| **Day 1** | Setup & Core | DB connected, Auth working, Files parsing |
| **Day 2** | Features | Skill analysis, AI integration, Resource APIs |
| **Day 3** | Complete Features | All endpoints working, Progress tracking |
| **Day 4** | Integration | Merged code, E2E testing, Bug fixes |
| **Day 5** | Polish & Present | Documentation, Presentation, Demo ready |

---

## 🚀 Let's Build PathForge Together!

Each file has comments explaining what to implement. Follow the PRD.md for requirements and DEVELOPMENT_GUIDE.md for setup instructions.

**Remember:** Quality over quantity. Write clean, tested, working code!
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
