import pytest
import requests
from constants import BASE_URL, SUPER_ADMIN
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator

@pytest.fixture(scope="session")
def session():
    http_session = requests.Session()
    http_session.base_url = BASE_URL
    yield http_session
    http_session.close()
    
@pytest.fixture(scope="session")
def api_manager(session):
    return ApiManager(session)

@pytest.fixture
def new_movies():
    return DataGenerator.valid_data_for_create_movies()

@pytest.fixture
def new_movies_min():
    return DataGenerator.min_valid_data_for_create_movies()

@pytest.fixture(scope="session")
def admin(api_manager):
    api_manager.auth_api.authenticate(SUPER_ADMIN)
    return api_manager

@pytest.fixture
def create_movies(admin, new_movies):
    return admin.movies_api.post_movies(json = new_movies).json()
