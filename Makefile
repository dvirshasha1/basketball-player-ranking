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
