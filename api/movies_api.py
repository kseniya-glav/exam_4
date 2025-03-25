from custom_requester.custom_requester import CustomRequester
from constants import MOVIES_ENDPOINT, MOVIES_ID_ENDPOINT, MOVIES_ID_REVIEWS_ENDPOINT, BASE_URL, BASE_HEADERS

class MoviesApi(CustomRequester):
    def __init__(self, session):
        super().__init__(base_url= BASE_URL, headers = BASE_HEADERS)
        self.session = session

    def get_movies(self, expected_status = 200, **kwargs):
        if (kwargs.get("headers")):
            self._update_session_headers(self.session, kwargs["headers"])
        return self.send_requests(
            method="GET",
            endpoint=MOVIES_ENDPOINT,
            expected_status=expected_status,
            **kwargs
        )
    
    def post_movies(self, expected_status = 200, **kwargs):
        if (kwargs.get("headers")):
            self._update_session_headers(self.session, kwargs["headers"])
        return self.send_requests(
            method="POST",
            endpoint=MOVIES_ENDPOINT,
            expected_status=expected_status,
            **kwargs
        )

    def get_movies_id(self, id, expected_status = 200, **kwargs):
        if (kwargs.get("headers")):
            self._update_session_headers(self.session, kwargs["headers"])
        return self.send_requests(
            method="GET",
            endpoint=MOVIES_ID_ENDPOINT.format(id = id),
            expected_status=expected_status,
            **kwargs
        )
    
    def delete_movies(self, id, expected_status = 200, **kwargs):
        if (kwargs.get("headers")):
            self._update_session_headers(self.session, kwargs["headers"])
        return self.send_requests(
            method="DELETE",
            endpoint=MOVIES_ID_ENDPOINT.format(id = id),
            expected_status=expected_status,
            **kwargs
        )

    def get_movies_reviews_id(self, id, expected_status = 200, **kwargs):
        if (kwargs.get("headers")):
            self._update_session_headers(self.session, kwargs["headers"])
        return self.send_requests(
            method="GET",
            endpoint=MOVIES_ID_REVIEWS_ENDPOINT.format(id = id),
            expected_status=expected_status,
            **kwargs
        )