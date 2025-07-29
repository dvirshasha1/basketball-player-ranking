#!/bin/bash

# Basketball Player Ranking - Repository Setup Script
# This script helps set up the GitHub repository with initial structure

#set -e  # Exit on any error

echo "🏀 Basketball Player Ranking - Repository Setup"
echo "================================================"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: This script should be run in the cloned GitHub repository"
    echo "Please run: git clone https://github.com/YOUR_USERNAME/basketball-player-ranking.git"
    echo "Then cd into the directory and run this script"
    exit 1
fi

echo "📁 Creating project directory structure..."

# Create backend structure
mkdir -p backend/{models,routes,services,utils}
mkdir -p backend/models backend/routes backend/services backend/utils

# Create frontend structure  
mkdir -p frontend/{public,src/{components,pages,services,styles,hooks,utils}}
mkdir -p frontend/src/{components,pages,services,styles,hooks,utils}

# Create database structure
mkdir -p database/{migrations,seeds}

# Create tests structure
mkdir -p tests/{backend,frontend,e2e}

# Create docs directory
mkdir -p docs

# Create initial Python files
touch backend/__init__.py
touch backend/app.py
touch backend/models/__init__.py
touch backend/models/player.py
touch backend/routes/__init__.py
touch backend/routes/players.py
touch backend/routes/stats.py
touch backend/services/__init__.py
touch backend/services/player_service.py
touch backend/services/scoring_service.py
touch backend/utils/__init__.py
touch backend/utils/validators.py

echo "📝 Creating configuration files..."

# Create requirements.txt
cat > requirements.txt << 'EOF'
# Web Framework
flask==2.3.3
flask-cors==4.0.0

# Database
pymongo==4.5.0
# OR for PostgreSQL: psycopg2-binary==2.9.7

# Data Validation
pydantic==2.4.2

# Environment Variables
python-dotenv==1.0.0

# API Documentation
flask-swagger-ui==4.11.1

# Development
python-json-logger==2.0.7
EOF

# Create requirements-dev.txt
cat > requirements-dev.txt << 'EOF'
# Testing
pytest==7.4.2
pytest-cov==4.1.0
pytest-asyncio==0.21.1

# Code Quality
black==23.9.1
flake8==6.1.0
mypy==1.6.1

# Development Tools
ipython==8.16.1
requests==2.31.0
EOF

# Create .env.example
cat > .env.example << 'EOF'
# Backend Configuration
DATABASE_URL=mongodb://localhost:27017/basketball_db
# For PostgreSQL: DATABASE_URL=postgresql://user:password@localhost:5432/basketball_db
API_SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
PORT=5000
FLASK_ENV=development

# Frontend Configuration
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_ENVIRONMENT=development

# Optional: External APIs
NBA_API_KEY=your-nba-api-key-here
EOF

# Create .gitignore (append to existing)
cat >> .gitignore << 'EOF'

# Project specific
.env
*.log
node_modules/
dist/
build/

# Python
__pycache__/
*.pyc
.pytest_cache/
.coverage
venv/
env/

# Frontend
.next/
.nuxt/
coverage/

# Database
*.db
*.sqlite3

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOF

# Create basic Makefile
cat > Makefile << 'EOF'
.PHONY: init install run_dev run_test run clean lint seed

# Colors for output
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[1;33m
BLUE=\033[0;34m
NC=\033[0m # No Color

init:
	@echo "$(GREEN)🏀 Initializing Basketball Player Ranking project...$(NC)"
	@echo "$(BLUE)Setting up Python virtual environment...$(NC)"
	python -m venv venv
	@echo "$(BLUE)Activating virtual environment and installing dependencies...$(NC)"
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -r requirements-dev.txt
	@echo "$(BLUE)Setting up frontend (when implemented)...$(NC)"
	@# cd frontend && npm install
	@echo "$(GREEN)✅ Project initialized successfully!$(NC)"
	@echo "$(YELLOW)Next steps:$(NC)"
	@echo "  1. Copy .env.example to .env and configure your settings"
	@echo "  2. Set up your database (MongoDB or PostgreSQL)"
	@echo "  3. Run 'make run_dev' to start development servers"

install:
	@echo "$(BLUE)Installing Python dependencies...$(NC)"
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -r requirements-dev.txt
	@echo "$(BLUE)Installing frontend dependencies...$(NC)"
	@# cd frontend && npm install

run_dev:
	@echo "$(GREEN)🚀 Starting development servers...$(NC)"
	@echo "$(YELLOW)Backend will be available at: http://localhost:5000$(NC)"
	@echo "$(YELLOW)Frontend will be available at: http://localhost:3000$(NC)"
	@echo "$(RED)Note: Backend and frontend implementation pending$(NC)"
	@# For now, just activate venv
	@echo "$(BLUE)Virtual environment activated. Start implementing!$(NC)"

run_test:
	@echo "$(BLUE)Running test suite...$(NC)"
	./venv/bin/pytest tests/ -v --cov=backend
	@# cd frontend && npm test

run:
	@echo "$(GREEN)🚀 Starting production server...$(NC)"
	@echo "$(RED)Production mode not implemented yet$(NC)"

clean:
	@echo "$(BLUE)Cleaning build artifacts...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache/ .coverage build/ dist/

lint:
	@echo "$(BLUE)Running code linters...$(NC)"
	./venv/bin/black backend/ --check
	./venv/bin/flake8 backend/
	@# cd frontend && npm run lint

seed:
	@echo "$(BLUE)Seeding database with sample data...$(NC)"
	@echo "$(RED)Database seeding not implemented yet$(NC)"
	@echo "$(YELLOW)Will be implemented in Issue #11$(NC)"

help:
	@echo "$(GREEN)Basketball Player Ranking - Available Commands:$(NC)"
	@echo "  $(BLUE)make init$(NC)     - Initialize the entire project"
	@echo "  $(BLUE)make install$(NC)  - Install all dependencies"
	@echo "  $(BLUE)make run_dev$(NC)  - Start development servers"
	@echo "  $(BLUE)make run_test$(NC) - Run test suite"
	@echo "  $(BLUE)make run$(NC)      - Start production server"
	@echo "  $(BLUE)make clean$(NC)    - Clean build artifacts"
	@echo "  $(BLUE)make lint$(NC)     - Run code linters"
	@echo "  $(BLUE)make seed$(NC)     - Seed database with sample data"
EOF

# Create enhanced README.md
cat > README.md << 'EOF'
# 🏀 Basketball Player Ranking System

A comprehensive web application for basketball player ranking and analysis featuring interactive spider charts, detailed player statistics, and modern web technologies.

![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-green)

## ✨ Features

- 🎯 **Interactive Player Cards** - Beautiful, responsive cards displaying key player statistics
- 📊 **Spider/Radar Charts** - Visualize offensive and defensive capabilities
- ➕ **Player Management** - Add, edit, and manage basketball players
- 🔍 **Advanced Search & Filtering** - Find players by name, team, position, and stats
- 📱 **Responsive Design** - Optimized for desktop, tablet, and mobile devices
- 🎨 **Modern UI** - Clean, professional interface with smooth animations

## 🛠️ Tech Stack

### Backend
- **Framework**: Python Flask/FastAPI
- **Database**: MongoDB or PostgreSQL
- **Validation**: Pydantic
- **Testing**: pytest

### Frontend
- **Framework**: React/Vue.js (TBD)
- **Charts**: Chart.js or D3.js
- **Styling**: Tailwind CSS
- **Testing**: Jest/Vitest

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- MongoDB or PostgreSQL
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/basketball-player-ranking.git
   cd basketball-player-ranking
   ```

2. **Initialize the project**
   ```bash
   make init
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your database settings
   ```

4. **Start development servers**
   ```bash
   make run_dev
   ```

5. **Access the application**
   - Backend API: http://localhost:5000
   - Frontend: http://localhost:3000

## 📖 Documentation

- [**Project Specification**](docs/OpenCode.md) - Comprehensive project documentation
- [**API Documentation**](docs/api.md) - API endpoints and schemas (coming soon)
- [**Development Guide**](docs/development.md) - Setup and development workflow (coming soon)

## 🧪 Testing

Run the complete test suite:
```bash
make run_test
```

Run specific test categories:
```bash
# Backend tests only
./venv/bin/pytest tests/backend/

# Frontend tests only (when implemented)
cd frontend && npm test
```

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `make init` | Initialize the entire project |
| `make install` | Install all dependencies |
| `make run_dev` | Start development servers |
| `make run_test` | Run test suite |
| `make clean` | Clean build artifacts |
| `make lint` | Run code linters |
| `make seed` | Seed database with sample data |

## 🗺️ Development Roadmap

### Phase 1: Foundation ✅
- [x] Project setup and architecture
- [ ] Backend API development
- [ ] Database schema and models

### Phase 2: Core Features (In Progress)
- [ ] Player management system
- [ ] Interactive UI components
- [ ] Data visualization charts

### Phase 3: Advanced Features (Planned)
- [ ] Search and filtering
- [ ] Player comparison tools
- [ ] Advanced statistics

### Phase 4: Polish & Production (Planned)
- [ ] UI/UX improvements
- [ ] Performance optimization
- [ ] Deployment configuration

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Project Structure

```
basketball-player-ranking/
├── backend/                 # Python backend application
│   ├── models/             # Database models
│   ├── routes/             # API endpoints
│   ├── services/           # Business logic
│   └── utils/              # Helper functions
├── frontend/               # Frontend application
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Application pages
│   │   └── services/       # API communication
├── database/               # Database scripts and migrations
├── tests/                  # Test files
├── docs/                   # Documentation
└── Makefile               # Development commands
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- NBA for providing inspiration for basketball statistics
- Open source community for amazing tools and libraries
- Contributors who help make this project better

## 📞 Support

If you have any questions or need help getting started:

1. Check the [Documentation](docs/)
2. Search existing [Issues](https://github.com/YOUR_USERNAME/basketball-player-ranking/issues)
3. Create a new [Issue](https://github.com/YOUR_USERNAME/basketball-player-ranking/issues/new)

---

**Happy Coding! 🏀**
EOF

# Copy the OpenCode.md to docs/
echo "📋 Adding project documentation..."
echo "# OpenCode.md - Basketball Player Ranking Web Application" > docs/OpenCode.md
echo "" >> docs/OpenCode.md
echo "This file should contain your original OpenCode.md content." >> docs/OpenCode.md
echo "Please copy the content from your original document to this file." >> docs/OpenCode.md

echo "✅ Repository structure created successfully!"
echo ""
echo "📋 Next Steps:"
echo "1. Copy your original OpenCode.md content to docs/OpenCode.md"
echo "2. Run: git add ."
echo "3. Run: git commit -m 'Initial project structure and documentation'"
echo "4. Run: git push origin main"
echo "5. Create GitHub issues using the detailed issue templates provided"
echo ""
echo "🚀 Then you can start development with:"
echo "   make init"
echo "   make run_dev"