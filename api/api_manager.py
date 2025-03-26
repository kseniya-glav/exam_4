from api.movies_api import MoviesApi
from api.auth_api import AuthAPI

class ApiManager:

    def __init__(self, session):
        self.session = session
        self.movies_api = MoviesApi(session)
        self.auth_api = AuthAPI(session)
