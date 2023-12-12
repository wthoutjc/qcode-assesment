import pytest
from src.init_app import init_app
from src.load_data import load_data

@pytest.fixture
def client():
    app = init_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            load_data()
            yield client    