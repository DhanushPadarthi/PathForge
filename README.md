# PathForge

**Tagline:** AI-forged learning roadmaps to your career

## Overview
PathForge is an AI-powered learning platform that helps students and fresh graduates build career-ready skills through personalized, deadline-based learning roadmaps. The platform supports users **with or without resumes**, analyzes skill gaps, and provides curated resources with real-time progress tracking.

## Problem Statement
Many students know their career goals but lack a clear and personalized path to achieve them. Existing platforms provide generic learning content, ignore current skills, and fail to track actual progress. PathForge solves this by providing AI-driven, personalized roadmaps tailored to individual skill levels and time availability.

## Key Features
- 📄 **Dual Entry Mode** - Upload resume OR answer basic questions to get started
- 🎯 **Skill Gap Analysis** - AI identifies what you need to learn for your career goal
- 🗺️ **Deadline-Based Roadmaps** - Time-aligned learning paths based on your availability
- 📚 **Curated Resources** - Relevant learning materials with external links
- ⏭️ **Smart Learning Flow** - Complete or skip topics you already know
- 📊 **Progress Tracking** - Visual progress bar tracking your learning journey
- 📝 **Module Summaries** - Get summaries after completing each module
- 👤 **User Dashboard** - See your roadmap, progress, and next steps
- 🔐 **Admin Panel** - Manage users, career roles, and learning resources

## Tech Stack

### Frontend
- React.js / Next.js
- CSS / Bootstrap
- Hosting: Vercel

### Backend
- Python (FastAPI)
- Resume extraction libraries (PDF/DOCX)
- API orchestration

### Database
- MongoDB Atlas

### Authentication
- Firebase Authentication

### File Storage
- Firebase Storage

### AI
- ChatGPT API

## Project Structure
```
PathForge/
├── backend/
│   ├── main.py                    # FastAPI app setup
│   ├── database.py                # MongoDB connection
│   ├── models.py                  # Database models/schemas
│   ├── requirements.txt           # Python dependencies
│   ├── routes/
│   │   ├── resume.py              # Resume upload & analysis
│   │   ├── roadmap.py             # Roadmap generation
│   │   ├── resources.py           # Resource management
│   │   └── admin.py               # Admin endpoints
│   └── services/
│       ├── resume_parser.py       # Resume parsing logic
│       ├── chatgpt_service.py     # AI integration
│       └── roadmap_service.py     # Roadmap business logic
├── frontend/
│   ├── package.json               # Frontend dependencies
│   └── src/
│       ├── pages/
│       │   ├── Landing.jsx        # Landing page
│       │   ├── Login.jsx          # Login page
│       │   ├── Dashboard.jsx      # Main dashboard
│       │   ├── Profile.jsx        # User profile
│       │   ├── Roadmap.jsx        # Roadmap display
│       │   ├── Resources.jsx      # Resources listing
│       │   └── Admin.jsx          # Admin dashboard
│       ├── components/
│       │   ├── Navbar.jsx         # Navigation bar
│       │   ├── ProgressBar.jsx    # Progress visualization
│       │   └── ResourceCard.jsx   # Resource card component
│       ├── services/
│       │   └── api.js             # API service layer
│       └── styles/
│           └── main.css           # Global styles
├── PRD.md                          # Product Requirements Document
├── README.md                       # This file
└── TEAM_ASSIGNMENTS.md            # Team collaboration guide
```

## Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- MongoDB Atlas account
- Firebase account
- OpenAI API key

### Backend Setup
```bash
cd backend
pip install -r requirements.txt

# Set up environment variables
# Create .env file with:
# - MONGODB_URI
# - OPENAI_API_KEY
# - FIREBASE_CONFIG

uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install

# Set up Firebase configuration
# Add Firebase config to your environment

npm start
```

## User Flow

### Flow 1: Student With Resume
User logs in → uploads resume → AI extracts skills → selects career goal & learning time → skill gaps identified → deadline-based roadmap generated → resources unlocked sequentially → completes or skips resources → progress tracked → module summary shown

### Flow 2: Student Without Resume
User logs in → answers basic questions → AI builds skill profile → selects career goal & learning time → skill gaps identified → deadline-based roadmap generated → resources unlocked sequentially → completes or skips resources → progress tracked → module summary shown

## Core Features (5-Day Scope)
1. ✅ Personalized learning roadmaps
2. ✅ Support for users with or without resumes
3. ✅ AI-powered skill gap analysis
4. ✅ Time-based resource delivery
5. ✅ Visual progress tracking
6. ✅ Module summaries
7. ✅ Admin panel for management

## Advanced Features (Future Scope)
- 🤖 **AI Mentor Chatbot** - Virtual mentor to keep users motivated
- 🚀 **AI Project Generator** - Generate resume-ready project ideas
- 📈 **Trending Skills Analyzer** - Show in-demand skills for career roles

## Team
- **Backend Team**: Dhanush (Lead), Varun - APIs, AI integration, database
- **Frontend Team**: Varsha, Mrinaliny - UI/UX, React components
- **UI/UX & Presentation**: Varshareddy - Design polish, documentation

## Documentation
- 📄 [Product Requirements Document (PRD)](PRD.md) - Complete product specifications
- 👥 [Team Assignments](TEAM_ASSIGNMENTS.md) - Team collaboration guide

## GitHub Repository
https://github.com/DhanushPadarthi/PathForge.git

## Success Metrics
- User onboarding completion rate
- Roadmap completion rate
- Learning consistency
- User feedback

## License
MIT

---

**PathForge - Your AI-powered career companion! 🚀**
