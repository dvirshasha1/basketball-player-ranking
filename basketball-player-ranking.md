# OpenCode.md - Basketball Player Ranking Web Application

## Project Overview
A comprehensive web application for basketball player ranking and analysis. The application allows users to view, add, and analyze basketball players with detailed statistics displayed through interactive spider charts and player cards.

## Architecture
**Three-tier architecture:**
- **Frontend**: Modern JavaScript framework (React/Vue/Angular) for dynamic UI
- **Backend**: Python-based API server for business logic and data processing
- **Database**: Flexible data storage for player statistics and metadata

## Project Structure
```
basketball-player-ranking/
├── Makefile                    # Task automation and commands
├── requirements.txt           # Python backend dependencies
├── requirements-dev.txt       # Development dependencies
├── backend/                   # Python backend (Flask/FastAPI/Django)
│   ├── __init__.py
│   ├── app.py                # Main application entry
│   ├── models/               # Data models and schemas
│   │   ├── __init__.py
│   │   └── player.py         # Player data model
│   ├── routes/               # API endpoints
│   │   ├── __init__.py
│   │   ├── players.py        # Player CRUD operations
│   │   └── stats.py          # Statistics calculations
│   ├── services/             # Business logic
│   │   ├── __init__.py
│   │   ├── player_service.py # Player management
│   │   └── scoring_service.py # Overall score calculations
│   └── utils/                # Helper functions
│       ├── __init__.py
│       └── validators.py     # Data validation
├── frontend/                 # Frontend application
│   ├── public/
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   │   ├── PlayerCard.js/vue
│   │   │   ├── SpiderChart.js/vue
│   │   │   └── PlayerForm.js/vue
│   │   ├── pages/            # Main application pages
│   │   │   ├── PlayerList.js/vue
│   │   │   ├── PlayerDetail.js/vue
│   │   │   └── AddPlayer.js/vue
│   │   └── services/         # API communication
│   │       └── api.js
├── database/                 # Database scripts and migrations
│   ├── migrations/
│   └── seeds/               # Sample data
├── tests/                   # Test files
│   ├── backend/
│   └── frontend/
├── docs/                    # Documentation
├── .env.example            # Environment variables template
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
└── OpenCode.md            # This file - OpenCode project memory
```

## Make Commands Reference

### `make init`
**Purpose**: Initialize the entire project environment
**What it does**:
- Sets up Python virtual environment for backend
- Installs Node.js dependencies for frontend
- Creates database and runs initial migrations
- Copies configuration templates (.env files)
- Sets up development environment

**Usage**: `make init`
**When to use**: First time setting up the project

### `make install`
**Purpose**: Install all project dependencies
**What it does**:
- Installs Python backend dependencies from requirements.txt
- Installs Node.js frontend dependencies from package.json
- Sets up development tools and pre-commit hooks

**Usage**: `make install`
**When to use**: After pulling new changes or when dependencies change

### `make run_dev`
**Purpose**: Start the full application in development mode
**What it does**:
- Starts Python backend server with hot reload (port 5000)
- Starts frontend development server with hot reload (port 3000)
- Enables debug mode, verbose logging
- Uses development database configuration

**Usage**: `make run_dev`
**When to use**: During active development

### `make run_test`
**Purpose**: Execute the complete test suite
**What it does**:
- Runs backend Python tests (pytest)
- Runs frontend JavaScript tests (Jest/Vitest)
- Generates test coverage reports
- Validates API endpoints and UI components

**Usage**: `make run_test`
**When to use**: Before committing code, during CI/CD

### `make run`
**Purpose**: Start the application in production mode
**What it does**:
- Starts optimized backend server (gunicorn/uvicorn)
- Serves built frontend static files
- Uses production database and configuration

**Usage**: `make run`
**When to use**: In production environments

## Basketball Player Data Model

### Player Schema
```python
{
    "id": "unique_identifier",
    "name": "Player Name",
    "team": "Team Name",
    "position": "PG/SG/SF/PF/C",
    "offense": {
        "shooting": 85,        # 0-100 rating
        "ball_handling": 78,
        "passing": 82,
        "speed": 90,
        "finishing": 88
    },
    "defense": {
        "perimeter_defense": 75,
        "interior_defense": 70,
        "steal": 80,
        "block": 65,
        "rebounding": 72
    },
    "overall_score": 79.5,    # Calculated from offense/defense
    "created_at": "timestamp",
    "updated_at": "timestamp"
}
```

### Overall Score Calculation
- **Offense Weight**: 50%
- **Defense Weight**: 50%
- **Formula**: `(avg(offense_stats) * 0.5) + (avg(defense_stats) * 0.5)`

## Development Phases & Tasks

### Phase 1: Project Foundation ✅
- [x] Environment setup (Python + Node.js)
- [x] Database design and API structure
- [x] Basic project scaffolding

### Phase 2: Core Frontend Development
- [ ] **Task 3**: Player Card Component
  - Display player name, team, position, overall score
  - Responsive card design with hover effects
- [ ] **Task 4**: Spider Chart Component  
  - Integrate Chart.js or D3.js for radar charts
  - Separate charts for offense and defense stats
- [ ] **Task 5**: Player List Display
  - Grid/list view of all players
  - Fetch data from backend API

### Phase 3: Interactive Features
- [ ] **Task 6**: Add New Player Form
  - Input fields for all player attributes
  - Form validation and error handling
- [ ] **Task 7**: Add Player Functionality
  - POST request to backend API
  - Real-time overall score calculation
  - Update player list after adding
- [ ] **Task 8**: Detailed Player View
  - Full player profile page
  - Complete spider charts display
  - Player statistics breakdown

### Phase 4: Search and Polish
- [ ] **Task 9**: Search Functionality
  - Search by name, team, position
  - Filter and sort capabilities
- [ ] **Task 10**: Styling and UX
  - Modern UI design (Tailwind/Bootstrap)
  - Mobile responsivity
  - Loading states and animations

## API Endpoints Design

### Player Management
```
GET    /api/players           # Get all players
GET    /api/players/:id       # Get specific player
POST   /api/players           # Create new player
PUT    /api/players/:id       # Update player
DELETE /api/players/:id       # Delete player
GET    /api/players/search    # Search players
```

### Statistics
```
GET    /api/stats/overview    # General statistics
GET    /api/stats/teams       # Team-based stats
POST   /api/stats/calculate   # Calculate overall scores
```

## Frontend Components Architecture

### Core Components
- **PlayerCard**: Compact player display with key stats
- **SpiderChart**: Interactive radar chart for detailed stats
- **PlayerForm**: Form for adding/editing players
- **SearchBar**: Search and filter functionality
- **PlayerList**: Grid/list container for multiple players

### Pages
- **Home**: Dashboard with overview and top players
- **Players**: Main player listing with search
- **PlayerDetail**: Individual player deep dive
- **AddPlayer**: Form for creating new players

## Development Workflow

### Initial Setup
```bash
make init     # Initialize full project
make install  # Install all dependencies
```

### Daily Development
```bash
make run_dev  # Start both backend and frontend
# Backend: http://localhost:5000
# Frontend: http://localhost:3000
make run_test # Test before committing
```

### Key Development Commands
```bash
# Backend only
cd backend && python app.py

# Frontend only  
cd frontend && npm run dev

# Database operations
python manage.py migrate
python manage.py seed_players
```

## Technology Stack

### Backend (Python)
- **Framework**: Flask/FastAPI/Django
- **Database**: MongoDB/PostgreSQL
- **ORM**: SQLAlchemy/Django ORM/Motor (for MongoDB)
- **Testing**: pytest, pytest-asyncio
- **Validation**: Pydantic/Marshmallow

### Frontend (JavaScript)
- **Framework**: React/Vue.js/Angular
- **Charts**: Chart.js or D3.js for spider charts
- **Styling**: Tailwind CSS/Material-UI/Bootstrap
- **HTTP Client**: Axios/Fetch API
- **Testing**: Jest/Vitest, React Testing Library

### Database
- **Primary**: MongoDB (flexible schema) or PostgreSQL (relational)
- **Caching**: Redis (optional for performance)

## Common Development Tasks

### Adding New Player Stats
1. Update player model/schema
2. Modify API validation
3. Update frontend form
4. Adjust spider chart component
5. Update overall score calculation

### Performance Optimization
- Implement pagination for player lists
- Add database indexing for search
- Cache frequently accessed data
- Optimize chart rendering

## Testing Strategy

### Backend Testing
- Unit tests for business logic
- API endpoint testing
- Database model validation
- Score calculation accuracy

### Frontend Testing  
- Component unit tests
- Integration tests for API calls
- UI interaction testing
- Chart rendering validation

## Deployment Notes

### Environment Variables
```bash
# Backend
DATABASE_URL=mongodb://localhost:27017/basketball_db
API_SECRET_KEY=your-secret-key
DEBUG=False

# Frontend
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_ENVIRONMENT=production
```

### Production Checklist
- [ ] Environment variables configured
- [ ] Database migrations applied
- [ ] Frontend built and optimized
- [ ] API rate limiting enabled
- [ ] Error monitoring setup
- [ ] Performance monitoring active

---

*Project Type: Basketball Player Ranking Web Application*
*Architecture: Full-stack with Python backend and JavaScript frontend*
*Last updated: [Current Date]*