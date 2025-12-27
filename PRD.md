# Product Requirements Document (PRD)

## Product Name: PathForge
**Tagline:** AI-forged learning roadmaps to your career

---

## 1. Purpose of the Product
The purpose of PathForge is to help students and fresh graduates achieve their career goals by providing a personalized, AI-driven learning roadmap based on their resume, existing skills, learning time, and chosen career path.

The platform guides users step by step using relevant learning resources, tracks progress visually, and avoids unnecessary content through skip options.

---

## 2. Problem Statement
Students and fresh graduates often know their career goals but lack a clear, personalized learning path to achieve them. Existing platforms provide generic courses, do not consider a user's current skills, and fail to track real learning progress. This leads to confusion, wasted time, and incomplete preparation for jobs.

There is a need for a system that understands a user's resume, identifies skill gaps, provides relevant learning resources, and tracks progress in a structured and adaptive way.

---

## 3. Solution Overview
PathForge is an AI-powered personalized learning and career roadmap platform that:
- Analyzes a user's resume using AI
- Identifies skill gaps for a selected career role
- Generates a time-based learning roadmap
- Recommends learning resources (links)
- Tracks progress with a progress bar
- Allows users to skip already known topics
- Helps users become job-ready efficiently

---

## 4. Target Users

### Primary Users
- College students
- Fresh graduates
- Career switchers

### Secondary Users
- Platform administrators
- Training institutions (future scope)

---

## 5. Key Objectives
1. Provide personalized learning paths instead of generic courses
2. Reduce confusion through structured roadmaps
3. Optimize learning based on available daily time
4. Track real learning progress visually
5. Improve job readiness effectively

---

## 6. User Roles

### 6.1 Student / Client
- Upload resume
- Select career goal and learning time
- Follow personalized roadmap
- Complete or skip resources
- Track progress

### 6.2 Admin
- Manage users
- Manage career roles and skills
- Manage learning resources
- Monitor platform analytics

---

## 7. Functional Requirements

### 7.1 Authentication
- Secure login using Email / Google
- Role-based access (User / Admin)
- Authentication handled by Firebase

### 7.2 Resume Upload & Processing
- Upload resume (PDF/DOCX)
- Resume stored securely
- Backend extracts text using Python

### 7.3 AI Resume Analysis
- Extract skills, education, and experience using ChatGPT API
- Store parsed data for further processing

### 7.4 Career Goal & Learning Time Selection
- User selects target career role
- User selects daily learning time (30 min / 1 hr / 2 hrs)

### 7.5 Skill Gap Analysis
- Compare user skills with required role skills
- Identify missing skills using AI

### 7.6 Personalized Roadmap Generation
- AI generates a step-by-step roadmap
- Roadmap aligned with learning time and skill gaps

### 7.7 Resource Recommendation
- AI recommends learning resources (external links)
- Each resource includes:
  - Title
  - Link
  - Estimated time

### 7.8 Learning Flow (NextWave-style)
- Sequential unlocking of resources
- User options:
  - Complete resource
  - Skip resource (already known)
- Automatic unlock of next resource

### 7.9 Progress Tracking
- Progress bar updates on completion/skip
- Completion percentage stored in real time

### 7.10 User Dashboard
- View roadmap and resources
- Track progress visually
- See next recommended step

### 7.11 Admin Panel
- View and manage users
- Add/update career roles
- Update skill requirements
- Review learning resources

---

## 8. Non-Functional Requirements
- Secure data handling
- Scalable architecture
- Fast response time
- Mobile-responsive UI
- High availability

---

## 9. Technology Stack (FINAL)

### Frontend
- React.js / Next.js
- CSS / Bootstrap
- Hosting: Vercel

### Authentication
- Firebase Authentication

### Backend
- Python – FastAPI
- Resume extraction libraries (PDF/DOCX)
- API orchestration

### Database
- MongoDB Atlas (Free Tier)

### File Storage
- Firebase Storage

### AI
- ChatGPT API

---

## 10. System Architecture Summary
PathForge uses a hybrid architecture where the frontend communicates with a Python FastAPI backend. Firebase handles authentication and resume storage, MongoDB stores application data, and ChatGPT API provides AI-driven resume analysis, skill gap detection, roadmap creation, and resource recommendations.

---

## 11. User Flow Summary
User logs in → uploads resume → AI extracts skills → user selects career goal & learning time → skill gaps identified → roadmap & resources generated → user completes or skips resources → progress tracked → job-ready user.

---

## 12. Security & Privacy
- Firebase Authentication for secure login
- API keys stored securely in backend environment variables
- Resume files stored securely
- Role-based access control

---

## 13. Assumptions & Constraints
- Internet access required
- AI outputs depend on resume quality
- Free-tier services may have usage limits

---

## 14. Future Enhancements
- Mock interviews
- Mentor guidance
- Placement tracking
- Mobile application
- Certification on completion
- Advanced analytics

---

## 15. Success Metrics
- User activation rate
- Roadmap completion rate
- Learning consistency
- User feedback and satisfaction

---

## 16. Final Summary
PathForge is a scalable, AI-powered learning platform that provides personalized career roadmaps, curated learning resources, and real-time progress tracking using a modern hybrid architecture with Python backend, MongoDB, Firebase services, and ChatGPT API.
