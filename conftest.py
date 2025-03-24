import pytest
import requests
from constants import BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT, AUTH_URL
from api.api_manager import ApiManager

@pytest.fixture(scope="session")
def session():
    http_session = requests.Session()
    http_session.base_url = BASE_URL
    yield http_session
    http_session.close()

@pytest.fixture(scope="session")
def api_manager(session):
    return ApiManager(session)

@pytest.fixture(scope="session")
def valid_data_for_create_movies():
    return {
        "name": "Название фильма",
        "imageUrl": "https://image.url",
        "price": 100,
        "description": "Описание фильма",
        "location": "SPB",
        "published": True,
        "genreId": 1
    }

@pytest.fixture(scope="session")
def min_valid_data_for_create_movies():
    return {
        "name": "Название фильма",
        "description": "Описание фильма",
        "location": "SPB",
        "published": True,
        "genreId": 1
    }
