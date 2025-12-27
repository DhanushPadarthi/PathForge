# PathForge - Team File Assignments

## AWS Mini Hackathon Team Structure

### Team Members & Branches
- **Dhanush**  - Branch: `dhanush`
- **Varsha** - Branch: `varsha`
- **Varshareddy** - Branch: `varshareddy`
- **Varun** - Branch: `varun`
- **Mrinaliny** - Branch: `mrinaliny`

---

## File Assignments

### 🎯 Dhanush (Lead) - Project Coordination & Integration
**Branch:** `dhanush`

**Backend Files:**
- `backend/main.py` - FastAPI app setup and route integration
- `backend/database.py` - MongoDB connection setup

**Frontend Files:**
- `frontend/src/pages/Dashboard.jsx` - Main dashboard page

**Responsibilities:**
- Set up project infrastructure
- Final integration and merging
- Code review and quality check

---

### 👤 Varsha - Authentication & User Management
**Branch:** `varsha`

**Backend Files:**
- `backend/routes/admin.py` - Admin endpoints

**Frontend Files:**
- `frontend/src/pages/Login.jsx` - Login page
- `frontend/src/pages/Profile.jsx` - User profile page
- `frontend/src/components/Navbar.jsx` - Navigation component

**Focus:**
- User authentication
- Profile management
- Admin panel UI

---

### 📝 Varshareddy - Resume Processing
**Branch:** `varshareddy`

**Backend Files:**
- `backend/routes/resume.py` - Resume upload/analysis endpoints
- `backend/services/resume_parser.py` - Resume parsing logic
- `backend/models.py` - Database models/schemas

**Frontend Files:**
- `frontend/src/pages/Landing.jsx` - Landing page

**Focus:**
- Resume upload functionality
- Resume parsing (PDF/DOCX)
- Skill extraction

---

### 🗺️ Varun - Roadmap & AI Integration
**Branch:** `varun`

**Backend Files:**
- `backend/routes/roadmap.py` - Roadmap generation endpoints
- `backend/services/chatgpt_service.py` - OpenAI/AI integration
- `backend/services/roadmap_service.py` - Roadmap business logic

**Frontend Files:**
- `frontend/src/pages/Roadmap.jsx` - Roadmap display page
- `frontend/src/components/ProgressBar.jsx` - Progress visualization

**Focus:**
- AI-powered roadmap generation
- Progress tracking
- Milestone management

---

### 📚 Mrinaliny - Resources & UI Components
**Branch:** `mrinaliny`

**Backend Files:**
- `backend/routes/resources.py` - Resource endpoints

**Frontend Files:**
- `frontend/src/pages/Resources.jsx` - Resources listing page
- `frontend/src/pages/Admin.jsx` - Admin dashboard
- `frontend/src/components/ResourceCard.jsx` - Resource card component
- `frontend/src/services/api.js` - API service layer
- `frontend/src/styles/main.css` - Global styles

**Focus:**
- Learning resources management
- UI components
- Styling and design

---

## Workflow Instructions

### For Team Members:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DhanushPadarthi/PathForge.git
   cd PathForge
   ```

2. **Switch to your branch:**
   ```bash
   git checkout <your-branch-name>
   ```
   Example: `git checkout varsha`

3. **Work on YOUR assigned files only**
   - You can see all files in the project
   - Only modify the files assigned to you
   - Don't change others' files to avoid merge conflicts

4. **Commit your changes regularly:**
   ```bash
   git add .
   git commit -m "Descriptive message about what you did"
   git push origin <your-branch-name>
   ```

5. **Pull latest changes from main:**
   ```bash
   git checkout main
   git pull origin main
   git checkout <your-branch-name>
   git merge main
   ```

### For Dhanush (Lead):

**Merging branches to main:**
```bash
# Switch to main
git checkout main

# Merge each team member's branch
git merge dhanush
git merge varsha
git merge varshareddy
git merge varun
git merge mrinaliny

# Resolve any conflicts if needed
# Push final version
git push origin main
```

---

## Communication Guidelines

- **Daily Updates:** Share progress in team chat
- **Blockers:** Report immediately if stuck
- **Code Review:** Request review before major changes
- **Testing:** Test your code before pushing
- **Documentation:** Comment your code properly

---

## Shared Resources

### Backend Dependencies
See `backend/requirements.txt`

### Frontend Dependencies
See `frontend/package.json`

### Environment Variables
Create `.env` file with:
```
MONGODB_URL=your_mongodb_url
OPENAI_API_KEY=your_openai_key
```

---

## Important Notes

⚠️ **DO NOT:**
- Push directly to `main` branch (only Dhanush)
- Modify files not assigned to you
- Delete or rename files without team discussion

✅ **DO:**
- Work only on your branch
- Pull latest changes regularly
- Communicate with team
- Write clean, documented code
- Test your changes

---

## GitHub Repository
https://github.com/DhanushPadarthi/PathForge.git

## Branches Created
- `main` - Production/Final code
- `dhanush` - Dhanush's workspace
- `varsha` - Varsha's workspace
- `varshareddy` - Varshareddy's workspace
- `varun` - Varun's workspace
- `mrinaliny` - Mrinaliny's workspace

---

**Good luck with the AWS Mini Hackathon! 🚀**
