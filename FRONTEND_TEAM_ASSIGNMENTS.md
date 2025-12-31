# PathForge - Frontend Team Assignments

## Phase 2: Frontend Development (CURRENT PRIORITY)

### Team Structure
- **Dhanush** - Frontend Lead - Branch: `dhanush`
- **Varun** - Frontend Developer - Branch: `varun`
- **Varsha** - Frontend Developer - Branch: `varsha`
- **Mrinaliny** - Frontend Developer - Branch: `mrinaliny`

---

## 💻 Dhanush (Frontend Lead) - Core App Setup & Authentication UI
**Branch:** `dhanush`

### Your Files:
- `frontend/src/App.jsx` - Main app with routing
- `frontend/src/main.jsx` - React DOM entry point
- `frontend/src/components/Auth/Login.jsx` - Login page
- `frontend/src/components/Auth/Register.jsx` - Registration page
- `frontend/src/components/Auth/ProtectedRoute.jsx` - Route protection
- `frontend/src/context/AuthContext.jsx` - Auth state management
- `frontend/src/services/authService.js` - Auth API calls
- `frontend/src/services/api.js` - Axios instance with interceptors
- `frontend/src/config/firebase.js` - Firebase client config
- `frontend/src/hooks/useAuth.js` - Custom auth hook
- `frontend/src/components/Navbar.jsx` - Navigation bar
- `frontend/vite.config.js` - Vite configuration
- `frontend/package.json` - Dependencies

### Key Responsibilities:
✅ React app initialization with Vite  
✅ React Router setup and navigation  
✅ Authentication UI (Login/Register)  
✅ Google OAuth integration  
✅ Firebase client SDK setup  
✅ Protected routes implementation  
✅ Axios instance with JWT interceptors  
✅ Context API for global state  
✅ Navigation bar with auth state  
✅ Error handling and validation  
✅ Toast notifications  
✅ Final integration and deployment  

### Tasks Checklist:
- [ ] Vite + React project setup
- [ ] React Router with protected routes
- [ ] Login page with email/password
- [ ] Register page with validation
- [ ] Google OAuth login button
- [ ] JWT token storage in localStorage
- [ ] Axios interceptors for auth headers
- [ ] AuthContext for global auth state
- [ ] useAuth custom hook
- [ ] Navbar with login/logout
- [ ] Protected route wrapper
- [ ] Form validation and error messages
- [ ] Loading states and spinners
- [ ] Toast notifications (react-hot-toast)

### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout dhanush

# Set up Node environment
cd frontend
npm install

# Daily workflow
git checkout dhanush
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented authentication UI and routing"
git push origin dhanush

# Run frontend dev server
npm run dev

# When merging all branches to main (Team Lead only)
git checkout main
git pull origin main
git merge dhanush
git merge varun
git merge varsha
git merge mrinaliny
git push origin main
```

---

## 💻 Varun - Resume Upload & Career Selection UI
**Branch:** `varun`

### Your Files:
- `frontend/src/components/Resume/ResumeUpload.jsx` - Resume upload
- `frontend/src/components/Resume/ResumePreview.jsx` - Resume preview
- `frontend/src/components/Career/CareerSelection.jsx` - Career selection
- `frontend/src/components/Common/FileUpload.jsx` - Reusable file upload
- `frontend/src/components/Common/Questionnaire.jsx` - Questionnaire form
- `frontend/src/services/resumeService.js` - Resume API calls
- `frontend/src/pages/HomePage.jsx` - Landing page
- `frontend/src/pages/Landing.jsx` - Welcome landing
- `frontend/src/utils/constants.js` - Career roles constants
- `frontend/src/utils/helpers.js` - Helper functions

### Key Responsibilities:
✅ Resume file upload with drag & drop  
✅ File validation (PDF/DOCX, size limits)  
✅ Resume parsing display  
✅ Career role selection UI  
✅ Questionnaire for no-resume flow  
✅ Landing page with two entry paths  
✅ Upload progress indicator  
✅ Career cards/grid layout  
✅ Integration with resume backend API  

### Tasks Checklist:
- [ ] Drag & drop file upload component
- [ ] File type validation (PDF/DOCX only)
- [ ] File size validation (max 5MB)
- [ ] Upload progress bar
- [ ] Resume preview after parsing
- [ ] Career role selection grid/cards
- [ ] Questionnaire form (no resume path)
- [ ] Landing page with two options
- [ ] Integration with /api/resume/upload
- [ ] Display extracted skills
- [ ] Error handling for failed uploads
- [ ] Loading spinners
- [ ] Responsive design for mobile

### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout varun

# Set up Node environment
cd frontend
npm install

# Daily workflow
git checkout varun
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented resume upload and career selection"
git push origin varun

# Run frontend dev server
npm run dev
```

---

## 💻 Varsha - Roadmap Display & AI Integration
**Branch:** `varsha`

### Your Files:
- `frontend/src/components/Roadmap/RoadmapView.jsx` - Main roadmap display
- `frontend/src/components/Roadmap/ModuleCard.jsx` - Module card
- `frontend/src/components/Roadmap/ResourceList.jsx` - Resources list
- `frontend/src/components/Roadmap/Timeline.jsx` - Visual timeline
- `frontend/src/context/RoadmapContext.jsx` - Roadmap state management
- `frontend/src/services/roadmapService.js` - Roadmap API calls
- `frontend/src/hooks/useRoadmap.js` - Custom roadmap hook
- `frontend/src/pages/RoadmapPage.jsx` - Roadmap page container
- `frontend/src/pages/Roadmap.jsx` - Roadmap wrapper
- `frontend/src/components/Common/LoadingSpinner.jsx` - Loading component
- `frontend/src/components/Common/EmptyState.jsx` - Empty state

### Key Responsibilities:
✅ Roadmap visualization with modules  
✅ Timeline display for learning path  
✅ Module cards with progress indicators  
✅ Resource list with lock/unlock states  
✅ AI-generated roadmap display  
✅ Sequential unlocking UI  
✅ Module completion status  
✅ Time-based module display (30min/1hr/2hr)  
✅ Interactive roadmap navigation  
✅ Integration with roadmap backend API  

### Tasks Checklist:
- [ ] Roadmap generation from backend
- [ ] Display modules in timeline format
- [ ] Module card with title, description, duration
- [ ] Lock/unlock icon for sequential modules
- [ ] Progress percentage display
- [ ] Resource list within each module
- [ ] AI summary display for each module
- [ ] Time commitment display
- [ ] Interactive module expand/collapse
- [ ] Completion checkmarks
- [ ] Integration with /api/roadmap endpoints
- [ ] RoadmapContext for state management
- [ ] Loading states during generation
- [ ] Empty state when no roadmap

### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout varsha

# Set up Node environment
cd frontend
npm install

# Daily workflow
git checkout varsha
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented roadmap visualization and timeline"
git push origin varsha

# Run frontend dev server
npm run dev
```

---

## 💻 Mrinaliny - Progress Tracking & Admin Dashboard
**Branch:** `mrinaliny`

### Your Files:
- `frontend/src/components/Progress/ProgressDashboard.jsx` - Progress overview
- `frontend/src/components/Progress/ProgressChart.jsx` - Progress charts
- `frontend/src/components/ProgressBar.jsx` - Reusable progress bar
- `frontend/src/components/ResourceCard.jsx` - Resource card
- `frontend/src/components/Admin/Dashboard.jsx` - Admin dashboard
- `frontend/src/components/Admin/UserManagement.jsx` - User management
- `frontend/src/components/Admin/CareerRoleManagement.jsx` - Role management
- `frontend/src/components/Admin/ResourceManagement.jsx` - Resource management
- `frontend/src/components/Admin/Statistics.jsx` - Platform statistics
- `frontend/src/services/progressService.js` - Progress API calls
- `frontend/src/services/adminService.js` - Admin API calls
- `frontend/src/hooks/useProgress.js` - Custom progress hook
- `frontend/src/pages/DashboardPage.jsx` - User dashboard page
- `frontend/src/pages/Dashboard.jsx` - Dashboard wrapper
- `frontend/src/pages/AdminPage.jsx` - Admin page container
- `frontend/src/pages/Admin.jsx` - Admin wrapper
- `frontend/src/pages/ProfilePage.jsx` - User profile page
- `frontend/src/pages/Profile.jsx` - Profile wrapper

### Key Responsibilities:
✅ User progress dashboard  
✅ Progress charts and visualizations  
✅ Resource completion tracking  
✅ Complete/Skip buttons functionality  
✅ Progress percentage calculation  
✅ Admin dashboard with statistics  
✅ User management CRUD UI  
✅ Career role management UI  
✅ Resource management UI  
✅ Platform analytics display  
✅ Charts and graphs (Chart.js/Recharts)  

### Tasks Checklist:
- [ ] Progress dashboard with stats
- [ ] Overall progress percentage
- [ ] Module-wise progress breakdown
- [ ] Progress charts (pie, bar, line)
- [ ] Resource card with complete/skip buttons
- [ ] Time spent tracking display
- [ ] Learning streak display
- [ ] Admin dashboard with key metrics
- [ ] User management table (view, delete)
- [ ] Career role CRUD interface
- [ ] Resource CRUD interface
- [ ] Platform statistics display
- [ ] Integration with /api/progress endpoints
- [ ] Integration with /api/admin endpoints
- [ ] Charts using Chart.js or Recharts
- [ ] Responsive admin layout

### Git Commands:
```bash
# Initial setup
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout mrinaliny

# Set up Node environment
cd frontend
npm install

# Daily workflow
git checkout mrinaliny
git pull origin main
# ... work on your files ...
git add .
git commit -m "Implemented progress tracking and admin dashboard"
git push origin mrinaliny

# Run frontend dev server
npm run dev
```

---

## Frontend Setup Instructions

### Prerequisites
- Node.js 18+ and npm
- Firebase project (same as backend)
- Backend API running on port 8000

### Setup Steps

1. **Clone Repository & Switch Branch**
```bash
git clone https://github.com/DhanushPadarthi/PathForge.git
cd PathForge
git checkout <your-branch-name>
```

2. **Install Dependencies**
```bash
cd frontend
npm install
```

3. **Create .env File**
```bash
# Create .env in frontend/ directory
VITE_API_URL=http://localhost:8000
VITE_FIREBASE_API_KEY=your_firebase_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id
VITE_ENVIRONMENT=development
```

4. **Run Development Server**
```bash
npm run dev
```

Frontend will run at: `http://localhost:5173`

---

## Daily Git Workflow

```bash
# 1. Start your day
git checkout <your-branch>
git pull origin main

# 2. Work on your files
# ... code, test, debug ...

# 3. Stage and commit
git add .
git commit -m "Implemented [feature name]"

# 4. Push to your branch
git push origin <your-branch>
```

---

## Frontend Dependencies

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.2",
    "firebase": "^10.7.1",
    "react-hot-toast": "^2.4.1",
    "recharts": "^2.10.3",
    "@headlessui/react": "^1.7.17",
    "@heroicons/react": "^2.1.1",
    "react-dropzone": "^14.2.3",
    "date-fns": "^2.30.0",
    "clsx": "^2.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0",
    "eslint": "^8.55.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32",
    "tailwindcss": "^3.3.6"
  }
}
```

---

## Frontend Routes Structure

| Route | Component | Owner |
|-------|-----------|-------|
| `/` | Landing page | Varun |
| `/login` | Login page | Dhanush |
| `/register` | Register page | Dhanush |
| `/home` | Home with resume choice | Varun |
| `/upload-resume` | Resume upload | Varun |
| `/questionnaire` | Questionnaire | Varun |
| `/career-selection` | Career selection | Varun |
| `/dashboard` | User dashboard | Mrinaliny |
| `/roadmap` | Roadmap view | Varsha |
| `/profile` | User profile | Mrinaliny |
| `/admin` | Admin dashboard | Mrinaliny |
| `/admin/users` | User management | Mrinaliny |
| `/admin/roles` | Role management | Mrinaliny |
| `/admin/resources` | Resource management | Mrinaliny |

---

## Timeline (Suggested)

### Day 1 (Current)
- **Dhanush**: Project setup, routing, auth pages
- **Varun**: Resume upload component, file validation
- **Varsha**: Roadmap visualization components
- **Mrinaliny**: Progress dashboard structure

### Day 2
- **Dhanush**: AuthContext, protected routes, Navbar
- **Varun**: Career selection, questionnaire
- **Varsha**: Module cards, timeline view
- **Mrinaliny**: Progress charts, resource cards

### Day 3
- **Dhanush**: API integration for auth
- **Varun**: Resume API integration
- **Varsha**: Roadmap API integration
- **Mrinaliny**: Progress API integration

### Day 4
- **All**: Admin panel components
- **All**: Testing and bug fixes
- **Dhanush**: Final integration

### Day 5
- **All**: Polish UI/UX
- **All**: Responsive design fixes
- **Dhanush**: Deploy frontend

---

## Important Guidelines

### ✅ DO:
- Work only on your assigned files
- Pull from main regularly
- Test before committing
- Write clear commit messages
- Ask for help when stuck
- Document your code
- Handle errors properly
- Make components responsive

### ⚠️ DO NOT:
- Push directly to `main` branch
- Modify files not assigned to you
- Commit without testing
- Share API keys in code (use .env)
- Delete others' work

---

**Focus on Frontend - Build Amazing User Interface! 🚀**
