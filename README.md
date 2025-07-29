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
