from backend import create_app
from backend.scripts.init_db import init_db

if __name__ == "__main__":
    app = create_app()
    init_db()
    app.run(port=5002, debug=True)
