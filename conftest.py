import pytest
import requests
from constants import BASE_URL, LOGIN_ENDPOINT, AUTH_URL, SUPER_ADMIN, BASE_HEADERS
from api.api_manager import ApiManager
from custom_requester.custom_requester import CustomRequester
import random

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
        "name": "Новый фильм" + str(random.uniform(-100000, 100000)),
        "imageUrl": "https://image.url",
        "price": 200,
        "description": "Описание фильма",
        "location": "SPB",
        "published": True,
        "genreId": 2
    }

@pytest.fixture(scope="session")
def min_valid_data_for_create_movies():
    return {
        "name": "Новый фильм" + str(random.uniform(-100000, 100000)),
        "price": 0,
        "description": "Описание фильма",
        "location": "SPB",
        "published": True,
        "genreId": 1
    }

@pytest.fixture(scope="session")
def super_admin_token(requester_auth):
    response = requester_auth.send_requests("POST", LOGIN_ENDPOINT, data = SUPER_ADMIN).json()
    if "accessToken" not in response:
        raise KeyError("token is missing")        
    token = response["accessToken"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture(scope="session")
def requester_auth():
    return CustomRequester(base_url = AUTH_URL, headers = BASE_HEADERS)

@pytest.fixture(scope="session")
def create_movies(api_manager, super_admin_token, valid_data_for_create_movies):
    response = api_manager.movies_api.post_movies(json = valid_data_for_create_movies, headers = super_admin_token, expected_status = 201)
    id_create_movie = response.json()["id"]
    response = api_manager.movies_api.get_movies_id(id_create_movie)
    assert response.json()["id"] == id_create_movie, "Фильма нет в списке"
    return response.json()
