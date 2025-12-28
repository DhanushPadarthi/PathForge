# PathForge Frontend

## Setup Instructions

### Prerequisites
- Node.js 16+ and npm/yarn
- Firebase account
- Backend API running

### Installation

1. Install dependencies:
```bash
npm install
# or
yarn install
```

2. Create `.env` file:
```bash
cp .env.example .env
```

3. Update `.env` with your configuration:
   - Firebase credentials
   - Backend API URL

### Running the Application

Development mode:
```bash
npm run dev
# or
yarn dev
```

Build for production:
```bash
npm run build
# or
yarn build
```

The application will be available at `http://localhost:5173`

## Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── Auth/           # Authentication components
│   │   ├── Resume/         # Resume upload components
│   │   ├── Career/         # Career selection
│   │   ├── Roadmap/        # Roadmap display
│   │   ├── Progress/       # Progress tracking
│   │   ├── Admin/          # Admin panel
│   │   └── Common/         # Shared components
│   ├── pages/              # Page components
│   ├── services/           # API services
│   ├── context/            # React context
│   ├── hooks/              # Custom hooks
│   ├── utils/              # Utility functions
│   └── config/             # Configuration
├── public/                  # Static assets
└── package.json            # Dependencies
```

## Technology Stack

- **React.js** - UI framework
- **Vite** - Build tool
- **Firebase** - Authentication & Storage
- **Axios** - HTTP client
- **React Router** - Routing

## Team Assignments

Refer to TEAM_ASSIGNMENTS.md for task allocation.
