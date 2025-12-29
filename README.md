# PathForge

**Tagline:** AI-forged learning roadmaps to your career

[![GitHub](https://img.shields.io/badge/GitHub-PathForge-blue)](https://github.com/DhanushPadarthi/PathForge)
[![Python](https://img.shields.io/badge/Python-3.9+-green)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-teal)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19.2-blue)](https://react.dev/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen)](https://www.mongodb.com/)

## 📝 Overview
PathForge is an AI-powered learning platform that helps students and fresh graduates build career-ready skills through personalized, deadline-based learning roadmaps. The platform supports users **with or without resumes**, analyzes skill gaps using ChatGPT, and provides curated resources with real-time progress tracking.

---

## 🎯 Problem Statement
Many students know their career goals but lack a clear and personalized path to achieve them. Existing platforms:
- ❌ Provide generic learning content
- ❌ Ignore current skill levels
- ❌ Fail to track actual progress
- ❌ Don't adapt to individual time availability

**PathForge solves this** by providing AI-driven, personalized roadmaps tailored to individual skill levels, career goals, and time availability.

---

## ✨ Key Features

### Core Features (v1.0)
- 📄 **Dual Entry Mode** - Upload resume OR answer questionnaire to get started
- 🤖 **AI Skill Extraction** - ChatGPT extracts skills from resume or questionnaire
- 🎯 **Skill Gap Analysis** - AI identifies what you need to learn for your career goal
- 🗺️ **Deadline-Based Roadmaps** - Time-aligned learning paths (30min/1hr/2hr daily)
- 📚 **AI Resource Recommendations** - Curated learning materials with external links
- ⏭️ **Smart Learning Flow** - Complete or skip topics you already know
- 📊 **Real-Time Progress Tracking** - Visual progress bar and completion percentages
- 📝 **Module Summaries** - AI-generated summaries after completing each module
- 👤 **Student Dashboard** - See roadmap, progress, and next steps
- 🔐 **Admin Panel** - Manage users, career roles, and learning resources
- 🔒 **Authentication** - Email/Password and Google OAuth login

### Advanced Features (Future Scope)
- 🤖 **AI Mentor Chatbot** - Virtual mentor to keep users motivated
- 🚀 **AI Project Generator** - Generate resume-ready project ideas
- 📈 **Trending Skills Analyzer** - Show in-demand skills for career roles

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: React.js 19.2 + Vite
- **Styling**: CSS / Bootstrap
- **State Management**: React Context API
- **HTTP Client**: Axios
- **Routing**: React Router
- **Authentication**: Firebase Authentication
- **Hosting**: Vercel

### Backend
- **Framework**: FastAPI 0.104
- **Language**: Python 3.9+
- **Async Runtime**: Uvicorn
- **Database Driver**: Motor (async MongoDB)
- **Resume Parsing**: PyPDF2, python-docx, pdfplumber
- **File Storage**: Firebase Storage
- **AI Integration**: OpenAI ChatGPT API
- **Authentication**: Firebase Admin SDK, JWT

### Database
- **Primary Database**: MongoDB Atlas
- **Schema**: Flexible document-based storage
- **Collections**: Users, Roadmaps, Resources, Progress, Skills, Career Roles

### DevOps & Tools
- **Version Control**: Git & GitHub
- **API Testing**: Postman / Thunder Client
- **Environment Management**: python-dotenv
- **Code Quality**: ESLint (Frontend), Black (Backend)

---

## 📂 Project Structure

```
PathForge/
├── backend/                           # Python FastAPI Backend
│   ├── app/
│   │   ├── main.py                   # FastAPI app initialization
│   │   ├── api/
│   │   │   └── routes/               # API endpoint routes
│   │   │       ├── auth.py          # Authentication (login, signup, OAuth)
│   │   │       ├── resume.py        # Resume upload & parsing
│   │   │       ├── skill_analysis.py # Skill gap analysis
│   │   │       ├── roadmap.py       # Roadmap generation
│   │   │       ├── resources.py     # Learning resources
│   │   │       ├── progress.py      # Progress tracking
│   │   │       └── admin.py         # Admin panel
│   │   ├── config/                   # Configuration files
│   │   │   ├── settings.py          # App settings & environment
│   │   │   ├── mongodb.py           # MongoDB connection
│   │   │   └── firebase.py          # Firebase Admin SDK
│   │   ├── core/                     # Core utilities
│   │   │   ├── security.py          # JWT, password hashing
│   │   │   └── dependencies.py      # FastAPI dependencies
│   │   ├── models/                   # Database models
│   │   │   ├── user.py              # User model
│   │   │   ├── roadmap.py           # Roadmap model
│   │   │   ├── resource.py          # Resource model
│   │   │   ├── progress.py          # Progress model
│   │   │   ├── skill.py             # Skill model
│   │   │   └── career_role.py       # Career role model
│   │   ├── schemas/                  # Pydantic schemas
│   │   │   ├── user_schema.py       # User request/response schemas
│   │   │   ├── roadmap_schema.py    # Roadmap schemas
│   │   │   ├── resource_schema.py   # Resource schemas
│   │   │   └── progress_schema.py   # Progress schemas
│   │   ├── services/                 # Business logic
│   │   │   ├── resume_parser.py     # PDF/DOCX parsing
│   │   │   ├── ai_service.py        # ChatGPT integration
│   │   │   ├── skill_analyzer.py    # Skill analysis logic
│   │   │   ├── roadmap_generator.py # Roadmap generation
│   │   │   ├── resource_recommender.py # Resource recommendations
│   │   │   └── progress_tracker.py  # Progress tracking
│   │   └── utils/                    # Helper utilities
│   │       ├── helpers.py           # General helpers
│   │       └── validators.py        # Input validation
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # Environment variables template
│   └── README.md                     # Backend documentation
│
├── frontend/                          # React Frontend
│   ├── src/
│   │   ├── components/               # React components
│   │   │   ├── Auth/                # Authentication components
│   │   │   │   ├── Login.jsx
│   │   │   │   ├── Register.jsx
│   │   │   │   └── ProtectedRoute.jsx
│   │   │   ├── Resume/              # Resume upload components
│   │   │   │   ├── ResumeUpload.jsx
│   │   │   │   └── QuestionForm.jsx
│   │   │   ├── Career/              # Career selection
│   │   │   │   └── CareerSelection.jsx
│   │   │   ├── Roadmap/             # Roadmap display
│   │   │   │   ├── RoadmapView.jsx
│   │   │   │   ├── ResourceCard.jsx
│   │   │   │   └── ModuleSummary.jsx
│   │   │   ├── Progress/            # Progress tracking
│   │   │   │   ├── ProgressBar.jsx
│   │   │   │   └── ProgressTracker.jsx
│   │   │   ├── Admin/               # Admin panel
│   │   │   │   ├── Dashboard.jsx
│   │   │   │   ├── UserManagement.jsx
│   │   │   │   ├── CareerRoleManagement.jsx
│   │   │   │   ├── ResourceManagement.jsx
│   │   │   │   └── Statistics.jsx
│   │   │   └── Common/              # Shared components
│   │   │       ├── Navbar.jsx
│   │   │       ├── Footer.jsx
│   │   │       └── Loader.jsx
│   │   ├── pages/                    # Page components
│   │   │   ├── HomePage.jsx         # Landing page
│   │   │   ├── DashboardPage.jsx    # Student dashboard
│   │   │   ├── RoadmapPage.jsx      # Roadmap view
│   │   │   ├── AdminPage.jsx        # Admin panel
│   │   │   └── ProfilePage.jsx      # User profile
│   │   ├── services/                 # API services
│   │   │   ├── api.js               # Axios configuration
│   │   │   ├── authService.js       # Auth API calls
│   │   │   ├── resumeService.js     # Resume API calls
│   │   │   ├── roadmapService.js    # Roadmap API calls
│   │   │   ├── progressService.js   # Progress API calls
│   │   │   └── adminService.js      # Admin API calls
│   │   ├── context/                  # React context
│   │   │   ├── AuthContext.jsx      # Auth state
│   │   │   └── RoadmapContext.jsx   # Roadmap state
│   │   ├── hooks/                    # Custom hooks
│   │   │   ├── useAuth.js
│   │   │   ├── useRoadmap.js
│   │   │   └── useProgress.js
│   │   ├── utils/                    # Utilities
│   │   │   ├── constants.js
│   │   │   └── helpers.js
│   │   ├── config/                   # Configuration
│   │   │   └── firebase.js          # Firebase config
│   │   ├── App.jsx                   # Main app component
│   │   └── main.jsx                  # Entry point
│   ├── package.json                  # Frontend dependencies
│   ├── vite.config.js               # Vite configuration
│   ├── .env.example                 # Environment template
│   └── README_FRONTEND.md           # Frontend documentation
│
├── PRD.md                            # Product Requirements Document
├── TEAM_ASSIGNMENTS.md              # Team collaboration guide
├── DEVELOPMENT_GUIDE.md             # Development setup guide
└── README.md                         # This file
```

---

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v16+)
- **Python** (v3.9+)
- **MongoDB Atlas** account
- **Firebase** project
- **OpenAI** API key

### Backend Setup

1. **Clone the Repository**
```bash
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge/backend
```

2. **Create Virtual Environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Variables**
```bash
# Copy example file
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux

# Edit .env and add:
# - MONGODB_URI
# - OPENAI_API_KEY
# - FIREBASE credentials
# - JWT_SECRET_KEY
```

5. **Run Backend Server**
```bash
uvicorn app.main:app --reload
```

Server runs at: **http://localhost:8000**  
API Docs: **http://localhost:8000/docs**

### Frontend Setup

1. **Navigate to Frontend**
```bash
cd PathForge/frontend
```

2. **Install Dependencies**
```bash
npm install
```

3. **Environment Variables**
```bash
# Copy example file
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux

# Edit .env and add:
# - VITE_FIREBASE_* credentials
# - VITE_API_URL=http://localhost:8000/api
```

4. **Run Frontend**
```bash
npm run dev
```

Frontend runs at: **http://localhost:5173**

---

## 📖 API Endpoints

### Authentication
- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/google` - Google OAuth
- `GET /api/auth/me` - Get current user
- `POST /api/auth/logout` - Logout

### Resume & Skills
- `POST /api/resume/upload` - Upload resume
- `POST /api/resume/parse` - Parse resume
- `POST /api/skills/analyze` - Analyze skills
- `POST /api/skills/gap-analysis` - Identify gaps
- `POST /api/skills/questionnaire` - Submit questionnaire

### Roadmap
- `POST /api/roadmap/generate` - Generate roadmap
- `GET /api/roadmap/{user_id}` - Get user roadmap
- `PUT /api/roadmap/{roadmap_id}` - Update roadmap
- `GET /api/roadmap/{roadmap_id}/modules` - Get modules

### Resources & Progress
- `GET /api/resources` - Get all resources
- `POST /api/resources/recommend` - Get recommendations
- `POST /api/progress/complete` - Mark complete
- `POST /api/progress/skip` - Skip resource
- `GET /api/progress/{user_id}` - Get progress

### Admin
- `GET /api/admin/users` - Get all users
- `GET /api/admin/statistics` - Platform stats
- `POST /api/admin/career-roles` - Add career role
- `POST /api/admin/resources` - Add resource

**Full API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs) (when backend is running)

---

---

## 🎭 User Flow

### Flow 1: Student With Resume
```
User logs in 
  → Uploads resume (PDF/DOCX) 
  → AI extracts skills using ChatGPT 
  → Selects career goal & daily learning time 
  → AI identifies skill gaps 
  → Deadline-based roadmap generated 
  → Learning modules created with milestones 
  → Resources unlocked sequentially 
  → Completes or skips resources 
  → Real-time progress tracked 
  → Module summary generated after completion 
  → Next module unlocked
```

### Flow 2: Student Without Resume
```
User logs in 
  → Answers basic questionnaire (skills, education, interests) 
  → AI builds skill profile 
  → Selects career goal & daily learning time 
  → AI identifies skill gaps 
  → Deadline-based roadmap generated 
  → Learning modules created with milestones 
  → Resources unlocked sequentially 
  → Completes or skips resources 
  → Real-time progress tracked 
  → Module summary generated after completion 
  → Next module unlocked
```

### Admin Flow
```
Admin logs in 
  → Accesses admin dashboard 
  → Views platform statistics 
  → Manages users (view, delete) 
  → Manages career roles (create, edit, delete) 
  → Manages learning resources (create, edit, delete) 
  → Views user progress and completion rates
```

---

## 🧑‍💻 Team

### Backend Team
- **Dhanush** (Lead) - Core backend setup, authentication, MongoDB, Firebase
- **Varun** - Resume processing, skill analysis, file parsing
- **Varsha** - AI integration, roadmap generation, ChatGPT service
- **Mrinaliny** - Resources, progress tracking, admin panel

### Documentation & Presentation
- **Varshareddy** - Presentation deck, documentation, demo preparation

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [PRD.md](PRD.md) | Complete product requirements and specifications |
| [TEAM_ASSIGNMENTS.md](TEAM_ASSIGNMENTS.md) | Team file assignments and Git workflow |
| [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md) | Detailed development setup guide |
| [backend/README.md](backend/README.md) | Backend-specific documentation |
| [frontend/README_FRONTEND.md](frontend/README_FRONTEND.md) | Frontend-specific documentation |

---

## 🔧 Development

### Backend Technologies
```python
# Core
FastAPI==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0

# Database
pymongo==4.6.0
motor==3.3.2  # Async MongoDB

# Authentication
firebase-admin==6.3.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4

# AI & Resume Parsing
openai==1.3.7
PyPDF2==3.0.1
python-docx==1.1.0
pdfplumber==0.10.3
```

### Frontend Technologies
```json
{
  "dependencies": {
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.0",
    "firebase": "^10.7.0"
  },
  "devDependencies": {
    "vite": "^7.2.4",
    "@vitejs/plugin-react": "^5.1.1"
  }
}
```

### Git Workflow
```bash
# Clone repository
git clone https://github.com/DhanushPadarthi/PathForge.git

# Create your branch (already created)
git checkout <your-branch>

# Daily workflow
git pull origin main
# ... make changes ...
git add .
git commit -m "Descriptive message"
git push origin <your-branch>
```

**Branches:**
- `main` - Production code
- `dhanush` - Core backend & auth
- `varun` - Resume & skills
- `varsha` - AI & roadmap
- `mrinaliny` - Resources & progress
- `varshareddy` - Documentation

---

## 🧪 Testing

### Backend Testing (Postman/Thunder Client)

**Test Authentication:**
```bash
POST http://localhost:8000/api/auth/signup
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "password123",
  "name": "Test User"
}
```

**Test Resume Upload:**
```bash
POST http://localhost:8000/api/resume/upload
Authorization: Bearer <your-token>
Content-Type: multipart/form-data

file: <select-pdf-or-docx>
```

**Test Roadmap Generation:**
```bash
POST http://localhost:8000/api/roadmap/generate
Authorization: Bearer <your-token>
Content-Type: application/json

{
  "career_role_id": "full-stack-developer",
  "learning_time": "1hr",
  "deadline": "2024-03-30"
}
```

### Frontend Testing
```bash
cd frontend
npm run dev

# Open browser at http://localhost:5173
# Test user flows manually
```

---

## 🎯 Development Status

### ✅ Completed
- [x] Project structure setup
- [x] File scaffolding
- [x] Documentation
- [x] Team assignments
- [x] Git repository setup
- [x] Development guidelines

### 🚧 In Progress (5-Day Timeline)
- [ ] Backend API implementation
- [ ] Frontend UI components
- [ ] AI integration
- [ ] Database models
- [ ] Authentication system

### 📅 Timeline
- **Day 1**: Setup & foundation (FastAPI, MongoDB, Auth structure)
- **Day 2**: Core features (Resume parsing, Skill analysis, AI service)
- **Day 3**: Advanced features (Roadmap generation, Progress tracking)
- **Day 4**: Integration & testing (Merge branches, bug fixes)
- **Day 5**: Final polish & presentation (Documentation, demo)

---

## 🐛 Troubleshooting

### Backend Issues

**MongoDB Connection Failed:**
```bash
# Check .env file
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/pathforge

# Verify IP whitelist in MongoDB Atlas (add 0.0.0.0/0 for testing)
```

**Python Dependencies:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --no-cache-dir --upgrade
```

**Port Already in Use:**
```bash
# Use different port
uvicorn app.main:app --reload --port 8001
```

### Frontend Issues

**Module Not Found:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Environment Variables:**
```bash
# Make sure .env file exists and has VITE_ prefix
VITE_API_URL=http://localhost:8000/api
```

---

## 📊 Success Metrics
- ✅ User onboarding completion rate
- ✅ Roadmap completion rate
- ✅ Learning consistency (daily active users)
- ✅ User feedback and satisfaction
- ✅ Time to first roadmap generation
- ✅ Average progress per week

---

## 🔮 Future Enhancements

### Phase 2 Features
- 🤖 **AI Mentor Chatbot** - Conversational assistant for motivation
- 🚀 **AI Project Generator** - Generate project ideas aligned with roadmap
- 📈 **Trending Skills** - Show in-demand skills for career roles
- 👥 **Peer Learning** - Connect with other learners
- 🏆 **Gamification** - Badges, streaks, and achievements
- 📱 **Mobile App** - Native iOS/Android apps
- 🔔 **Push Notifications** - Reminders and motivational messages
- 📊 **Advanced Analytics** - Detailed learning insights

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Code Style:**
- Backend: Follow PEP 8 (Python)
- Frontend: Follow ESLint configuration
- Commit messages: Clear and descriptive

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Contact & Links

- **GitHub Repository**: [https://github.com/DhanushPadarthi/PathForge](https://github.com/DhanushPadarthi/PathForge)
- **Team Lead**: Dhanush
- **Project Type**: AWS Mini Hackathon Project
- **Development Period**: 5 Days
- **Tech Focus**: AI-Powered Learning Platform

---

## 🙏 Acknowledgments

- **OpenAI** - For ChatGPT API
- **MongoDB Atlas** - For database hosting
- **Firebase** - For authentication and storage
- **FastAPI** - For excellent Python framework
- **React** - For modern frontend development

---

<div align="center">

### PathForge - Your AI-powered career companion! 🚀

**Built with ❤️ by Team PathForge**

[![GitHub Stars](https://img.shields.io/github/stars/DhanushPadarthi/PathForge?style=social)](https://github.com/DhanushPadarthi/PathForge)
[![GitHub Forks](https://img.shields.io/github/forks/DhanushPadarthi/PathForge?style=social)](https://github.com/DhanushPadarthi/PathForge)

</div>
