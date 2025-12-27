# PathForge - Team File Assignments

## AWS Mini Hackathon Team Structure

### Team Members & Branches
- **Dhanush** - Backend Team - Branch: `dhanush`
- **Varun** - Backend Team - Branch: `varun`
- **Varsha** - Frontend Team - Branch: `varsha`
- **Mrinaliny** - Frontend Team - Branch: `mrinaliny`
- **Varshareddy** - UI/UX & Presentation - Branch: `varshareddy`

---

## Team Divisions

### 🔧 Backend Team
**Members:** Dhanush & Varun

### 🎨 Frontend Team
**Members:** Varsha & Mrinaliny

### 🎯 UI/UX & Presentation
**Member:** Varshareddy

---

## File Assignments

### 🔧 Dhanush (Lead) - Backend Development & Integration
**Branch:** `dhanush`  
**Team:** Backend

**Your Files:**
- `backend/main.py` - FastAPI app setup and route integration
- `backend/database.py` - MongoDB connection setup
- `backend/models.py` - Database models/schemas
- `backend/routes/resume.py` - Resume upload/analysis endpoints
- `backend/services/resume_parser.py` - Resume parsing logic

**Responsibilities:**
- FastAPI application setup
- Database integration
- Resume processing backend
- Final integration and merging
- Code review and quality check

**Your Commands:**
```bash
# Step 1: Clone the repository
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge

# Step 2: Switch to your branch
git checkout dhanush

# Step 3: Work on your files (edit backend files assigned to you)

# Step 4: Check what files you changed
git status

# Step 5: Add your changes
git add .

# Step 6: Commit your changes
git commit -m "Description of what you did"

# Step 7: Push to your branch
git push origin dhanush

# When ready to merge everyone's work:
git checkout main
git pull origin main
git merge dhanush
git merge varun
git merge varsha
git merge mrinaliny
git merge varshareddy
git push origin main
```

---

### 🔧 Varun - Backend Development (Roadmap & AI)
**Branch:** `varun`  
**Team:** Backend

**Your Files:**
- `backend/routes/roadmap.py` - Roadmap generation endpoints
- `backend/routes/resources.py` - Resource endpoints
- `backend/routes/admin.py` - Admin endpoints
- `backend/services/chatgpt_service.py` - OpenAI/AI integration
- `backend/services/roadmap_service.py` - Roadmap business logic
- `backend/requirements.txt` - Python dependencies

**Responsibilities:**
- AI-powered roadmap generation
- Learning resources API
- Admin panel backend
- OpenAI integration
- API endpoint development

**Your Commands:**
```bash
# Step 1: Clone the repository
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge

# Step 2: Switch to your branch
git checkout varun

# Step 3: Work on your files (edit backend files assigned to you)

# Step 4: Check what files you changed
git status

# Step 5: Add your changes
git add .

# Step 6: Commit your changes
git commit -m "Description of what you did"

# Step 7: Push to your branch
git push origin varun

# To get latest changes from main:
git checkout main
git pull origin main
git checkout varun
git merge main
```

---

### 🎨 Varsha - Frontend Development (Auth & User Pages)
**Branch:** `varsha`  
**Team:** Frontend

**Your Files:**
- `frontend/src/pages/Landing.jsx` - Landing page
- `frontend/src/pages/Login.jsx` - Login page
- `frontend/src/pages/Profile.jsx` - User profile page
- `frontend/src/pages/Dashboard.jsx` - Main dashboard page
- `frontend/src/components/Navbar.jsx` - Navigation component

**Responsibilities:**
- User authentication UI
- Landing page design
- Profile management interface
- Dashboard layout
- Navigation component

**Your Commands:**
```bash
# Step 1: Clone the repository
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge

# Step 2: Switch to your branch
git checkout varsha

# Step 3: Work on your files (edit frontend files assigned to you)

# Step 4: Check what files you changed
git status

# Step 5: Add your changes
git add .

# Step 6: Commit your changes
git commit -m "Description of what you did"

# Step 7: Push to your branch
git push origin varsha

# To get latest changes from main:
git checkout main
git pull origin main
git checkout varsha
git merge main
```

---

### 🎨 Mrinaliny - Frontend Development (Features & Components)
**Branch:** `mrinaliny`  
**Team:** Frontend

**Your Files:**
- `frontend/src/pages/Roadmap.jsx` - Roadmap display page
- `frontend/src/pages/Resources.jsx` - Resources listing page
- `frontend/src/pages/Admin.jsx` - Admin dashboard
- `frontend/src/components/ProgressBar.jsx` - Progress visualization
- `frontend/src/components/ResourceCard.jsx` - Resource card component
- `frontend/src/services/api.js` - API service layer
- `frontend/package.json` - Frontend dependencies

**Responsibilities:**
- Roadmap visualization
- Resources page
- Admin panel UI
- Reusable components
- API integration layer
- Frontend package management

**Your Commands:**
```bash
# Step 1: Clone the repository
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge

# Step 2: Switch to your branch
git checkout mrinaliny

# Step 3: Work on your files (edit frontend files assigned to you)

# Step 4: Check what files you changed
git status

# Step 5: Add your changes
git add .

# Step 6: Commit your changes
git commit -m "Description of what you did"

# Step 7: Push to your branch
git push origin mrinaliny

# To get latest changes from main:
git checkout main
git pull origin main
git checkout mrinaliny
git merge main
```

---

### 🎯 Varshareddy - UI/UX Polish & Presentation
**Branch:** `varshareddy`  
**Team:** UI/UX & Presentation

**Your Files:**
- `frontend/src/styles/main.css` - Global styles and design
- `docs/PRD.md` - Product Requirements Document
- `docs/API.md` - API Documentation
- `README.md` - Project documentation

**Additional Tasks:**
- Create presentation (PPT/Slides)
- Design improvements
- Color scheme and branding
- Documentation polishing
- Demo preparation

**Responsibilities:**
- Overall UI/UX consistency
- Styling and design polish
- Creating presentation for hackathon
- Documentation and README
- Final demo preparation

**Your Commands:**
```bash
# Step 1: Clone the repository
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge

# Step 2: Switch to your branch
git checkout varshareddy

# Step 3: Work on your files (edit CSS, docs, and create PPT)

# Step 4: Check what files you changed
git status

# Step 5: Add your changes (including PPT if you put it in docs/)
git add .

# Step 6: Commit your changes
git commit -m "Description of what you did"

# Step 7: Push to your branch
git push origin varshareddy

# To get latest changes from main:
git checkout main
git pull origin main
git checkout varshareddy
git merge main
```

---

## Quick Start for Everyone

### First Time Setup (Do this once)

**Step 1:** Open Terminal/Command Prompt/Git Bash

**Step 2:** Clone the repository
```bash
git clone https://github.com/DhanushPadarthi/PathForge.git
```

**Step 3:** Navigate to project folder
```bash
cd PathForge
```

**Step 4:** Switch to YOUR branch (use your name)
```bash
# For Dhanush:
git checkout dhanush

# For Varun:
git checkout varun

# For Varsha:
git checkout varsha

# For Mrinaliny:
git checkout mrinaliny

# For Varshareddy:
git checkout varshareddy
```

---

## Daily Workflow (Every time you work)

### 1️⃣ Before You Start Working
```bash
# Make sure you're on your branch
git checkout <your-branch-name>

# Get latest changes from main
git pull origin main
```

### 2️⃣ While Working
- Open and edit ONLY the files assigned to you
- You can see all files but only change YOUR files
- Save your work frequently

### 3️⃣ After Making Changes
```bash
# See what files you changed
git status

# Add all your changes
git add .

# Commit with a clear message
git commit -m "Added login functionality" 
# Or: "Fixed navbar styling"
# Or: "Implemented resume parser"

# Push to YOUR branch
git push origin <your-branch-name>
```

---

## Example: Complete Workflow for Varsha

```bash
# Day 1 - First time
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout varsha
# ... work on Login.jsx ...
git add .
git commit -m "Created login page UI"
git push origin varsha

# Day 2 - Next day
cd PathForge
git checkout varsha
git pull origin main
# ... work on Profile.jsx ...
git add .
git commit -m "Added profile page with user info"
git push origin varsha

# Day 3 - Continue
cd PathForge
git checkout varsha
git pull origin main
# ... improve Dashboard.jsx ...
git add .
git commit -m "Enhanced dashboard with charts"
git push origin varsha
```

---

## Backend Team - Additional Setup

**Dhanush & Varun:** After cloning, set up Python environment:

```bash
cd PathForge/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
uvicorn main:app --reload
```

---

## Frontend Team - Additional Setup

**Varsha & Mrinaliny:** After cloning, set up React environment:

```bash
cd PathForge/frontend

# Install dependencies
npm install

# Run the development server
npm start
```

---

## Common Git Commands Reference

| Command | What it does |
|---------|-------------|
| `git status` | See what files you changed |
| `git add .` | Stage all your changes |
| `git commit -m "message"` | Save your changes with a message |
| `git push origin <branch>` | Upload your changes to GitHub |
| `git pull origin main` | Download latest changes from main |
| `git checkout <branch>` | Switch to a branch |
| `git log` | See history of commits |

---

## Troubleshooting

### Problem: "Already have a folder named PathForge"
```bash
# Delete the old folder or rename it
cd PathForge
git pull origin main
git checkout <your-branch>
```

### Problem: "Cannot push, need to pull first"
```bash
git pull origin <your-branch>
git push origin <your-branch>
```

### Problem: "Merge conflict"
```bash
# Ask Dhanush for help!
# Or manually edit the conflicted files and:
git add .
git commit -m "Resolved merge conflict"
git push origin <your-branch>
```

### Problem: "Accidentally changed someone else's file"
```bash
# Undo changes to a specific file
git checkout HEAD -- path/to/file
```

---

## Communication Guidelines

- **Daily Updates:** Share progress in team chat
- **Blockers:** Report immediately if stuck
- **Code Review:** Request review before major changes
- **Testing:** Test your code before pushing
- **Documentation:** Comment your code properly

---

## Important Notes

⚠️ **DO NOT:**
- Push directly to `main` branch (only Dhanush merges)
- Modify files not assigned to you
- Delete or rename files without team discussion
- Commit without testing your code

✅ **DO:**
- Work only on your branch
- Pull latest changes regularly from main
- Communicate with team daily
- Write clean, documented code
- Test your changes before pushing
- Use clear commit messages

---

## GitHub Repository
https://github.com/DhanushPadarthi/PathForge.git

## Branches Created
- `main` - Production/Final code (Dhanush merges here)
- `dhanush` - Dhanush's workspace (Backend Lead)
- `varun` - Varun's workspace (Backend)
- `varsha` - Varsha's workspace (Frontend)
- `mrinaliny` - Mrinaliny's workspace (Frontend)
- `varshareddy` - Varshareddy's workspace (UI/UX & PPT)

---

**Good luck with the AWS Mini Hackathon! 🚀**
