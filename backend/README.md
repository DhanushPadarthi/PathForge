# PathForge Backend

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- MongoDB Atlas account
- Firebase account
- OpenAI API key

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Update `.env` with your credentials:
   - MongoDB URI
   - Firebase credentials
   - OpenAI API key
   - JWT secret key

### Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── routes/          # API endpoints
│   ├── config/              # Configuration files
│   ├── core/                # Core utilities (security, dependencies)
│   ├── models/              # Database models
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   └── utils/               # Helper functions
├── requirements.txt         # Python dependencies
└── .env.example            # Environment variables template
```

## Team Assignments

Refer to TEAM_ASSIGNMENTS.md for task allocation.
