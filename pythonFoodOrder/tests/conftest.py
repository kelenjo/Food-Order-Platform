import tempfile
import os
import pytest
from src import create_app
from src.ext import admin
from src.commands import init_db, populate_db


@pytest.fixture
def app():
    # Create a temporary file
    db_fd, db_path = tempfile.mkstemp()

    test_config = {
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
        "DEBUG": False,
        "SECRET_KEY": "test-secret-key",
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}.sqlite",  # Use temporary SQLite file
    }

    app = create_app(test_config=test_config)
    admin._views = []

    with app.app_context():
        init_db()
        populate_db()

    yield app

    # Cleanup
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def server(app):
    return app.test_cli_runner()
