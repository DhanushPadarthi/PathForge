# PathForge - Development Guide

## Getting Started

This guide will help team members set up and contribute to the PathForge project.

### Repository Structure

```
PathForge/
├── backend/                 # Python FastAPI backend
├── frontend/                # React frontend
├── PRD.md                   # Product Requirements Document
├── README.md                # Main project documentation
└── TEAM_ASSIGNMENTS.md      # Task assignments
```

### Initial Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd PathForge
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Update .env with your credentials
```

3. **Frontend Setup**
```bash
cd frontend
npm install
cp .env.example .env
# Update .env with your credentials
```

### Development Workflow

1. **Create a feature branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**
   - Write code in the assigned files
   - Follow coding standards
   - Add comments where necessary

3. **Test your changes**
   - Backend: Run tests and manual testing
   - Frontend: Test components in browser

4. **Commit and push**
```bash
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

5. **Create Pull Request**
   - Go to GitHub and create a PR
   - Request review from team members
   - Address feedback

### Coding Standards

#### Backend (Python)
- Follow PEP 8 style guide
- Use type hints
- Write docstrings for functions
- Use meaningful variable names

#### Frontend (JavaScript/React)
- Use ES6+ syntax
- Follow React best practices
- Use functional components and hooks
- Write descriptive component names

### File Structure Overview

#### Backend Files to Implement

**Configuration:**
- `app/config/settings.py` - App settings
- `app/config/firebase.py` - Firebase setup
- `app/config/mongodb.py` - Database connection

**API Routes:**
- `app/api/routes/auth.py` - Authentication endpoints
- `app/api/routes/resume.py` - Resume processing
- `app/api/routes/skill_analysis.py` - Skill analysis
- `app/api/routes/roadmap.py` - Roadmap generation
- `app/api/routes/resources.py` - Learning resources
- `app/api/routes/progress.py` - Progress tracking
- `app/api/routes/admin.py` - Admin panel

**Services:**
- `app/services/resume_parser.py` - Resume parsing
- `app/services/ai_service.py` - ChatGPT integration
- `app/services/skill_analyzer.py` - Skill analysis
- `app/services/roadmap_generator.py` - Roadmap creation
- `app/services/resource_recommender.py` - Resource recommendations
- `app/services/progress_tracker.py` - Progress management

#### Frontend Files to Implement

**Components:**
- `components/Auth/` - Login, Register, Protected routes
- `components/Resume/` - Resume upload, Questionnaire
- `components/Career/` - Career selection
- `components/Roadmap/` - Roadmap view, Resources
- `components/Progress/` - Progress tracking
- `components/Admin/` - Admin panel components

**Pages:**
- `pages/HomePage.jsx` - Landing page
- `pages/DashboardPage.jsx` - Student dashboard
- `pages/RoadmapPage.jsx` - Roadmap view
- `pages/AdminPage.jsx` - Admin panel
- `pages/ProfilePage.jsx` - User profile

**Services:**
- `services/authService.js` - Authentication API calls
- `services/resumeService.js` - Resume API calls
- `services/roadmapService.js` - Roadmap API calls
- `services/progressService.js` - Progress API calls
- `services/adminService.js` - Admin API calls

### Environment Variables

#### Backend (.env)
- `MONGODB_URI` - MongoDB connection string
- `FIREBASE_*` - Firebase credentials
- `OPENAI_API_KEY` - OpenAI API key
- `SECRET_KEY` - JWT secret
- `ALLOWED_ORIGINS` - CORS origins

#### Frontend (.env)
- `VITE_FIREBASE_*` - Firebase credentials
- `VITE_API_URL` - Backend API URL

### Testing

#### Backend Testing
```bash
cd backend
pytest
```

#### Frontend Testing
```bash
cd frontend
npm test
```

### Common Issues & Solutions

1. **CORS errors**: Update ALLOWED_ORIGINS in backend .env
2. **Firebase errors**: Verify Firebase credentials
3. **MongoDB connection**: Check MongoDB URI and network access
4. **API not responding**: Ensure backend server is running

### Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [MongoDB Documentation](https://docs.mongodb.com/)

### Getting Help

- Check existing issues on GitHub
- Ask in team chat
- Refer to PRD.md for requirements
- Check TEAM_ASSIGNMENTS.md for task details

## Next Steps

1. Review assigned tasks in TEAM_ASSIGNMENTS.md
2. Set up development environment
3. Read relevant documentation
4. Start implementing assigned features
5. Communicate progress with team

Good luck with development! 🚀
