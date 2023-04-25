import pytest
from app.app import create_app
from os import environ
from flask_migrate import upgrade


# define fixture setting up in-memory database
@pytest.fixture
def client():
    environ["DATABASE_URL"] = "sqlite://"
    app = create_app()

    with app.app_context():
        upgrade()
        yield app.test_client()
