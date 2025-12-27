# PathForge

**Tagline:** AI-forged learning roadmaps to your career

## Overview
PathForge is an AI-powered personalized learning and career roadmap platform that helps students and fresh graduates achieve their career goals. The platform analyzes your resume using AI, identifies skill gaps, generates a time-based learning roadmap, and provides curated learning resources with real-time progress tracking.

## Problem Statement
Students and fresh graduates often know their career goals but lack a clear, personalized learning path. Existing platforms provide generic courses, don't consider current skills, and fail to track real progress. PathForge solves this by providing AI-driven, personalized roadmaps tailored to individual skill levels and time availability.

## Key Features
- 📄 **Resume Analysis** - Upload your resume (PDF/DOCX) and let AI extract your skills and experience
- 🎯 **Skill Gap Analysis** - Compare your skills with target career role requirements
- 🗺️ **Personalized Roadmaps** - AI-generated learning paths based on your time availability
- 📚 **Curated Resources** - Get relevant learning resources with external links
- ⏭️ **Smart Learning Flow** - Complete or skip topics you already know
- 📊 **Progress Tracking** - Visual progress bar to track your learning journey
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
- MongoDB Atlas (Free Tier)

### Authentication
- Firebase Authentication

### File Storage
- Firebase Storage

### AI
- ChatGPT API

## Project Structure
```
PathForge/
├── frontend/          # React frontend
├── backend/           # FastAPI backend
└── docs/              # Documentation
```

## Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- MongoDB

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Documentation
- 📄 [Product Requirements Document (PRD)](docs/PRD.md) - Complete product specifications
- 🔌 [API Documentation](docs/API.md) - Backend API reference
- 👥 [Team Assignments](TEAM_ASSIGNMENTS.md) - Team collaboration guide

## Team
- **Backend Team**: Dhanush (Lead), Varun - APIs, AI integration, database
- **Frontend Team**: Varsha, Mrinaliny - UI/UX, React components
- **UI/UX & Presentation**: Varshareddy - Design polish, PPT preparation

## GitHub Repository
https://github.com/DhanushPadarthi/PathForge.git

## User Flow
User logs in → uploads resume → AI extracts skills → user selects career goal & learning time → skill gaps identified → roadmap & resources generated → user completes or skips resources → progress tracked → job-ready user.

## License
MIT

---

**Good luck with the AWS Mini Hackathon! 🚀**
