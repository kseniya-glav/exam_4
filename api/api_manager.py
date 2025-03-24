from api.movies_api import MoviesApi

class ApiManager:

    def __init__(self, session):
        self.session = session
        self.movies_api = MoviesApi(session)
