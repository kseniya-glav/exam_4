from custom_requester.custom_requester import CustomRequester
from constants import MOVIES_ENDPOINT, MOVIES_ID_ENDPOINT, MOVIES_ID_REVIEWS_ENDPOINT, BASE_URL, BASE_HEADERS

class MoviesApi(CustomRequester):
    def __init__(self, session):
        super().__init__(base_url= BASE_URL, headers = BASE_HEADERS)
        self.session = session

    def get_movies(self, params = None, headers = None, expected_status = 200):

        return self.send_requests(
            method="GET",
            endpoint=MOVIES_ENDPOINT,
            params=params,
            headers=headers,
            expected_status=expected_status
        )
    
    def post_movies(self, data = None, params = None, headers = None, expected_status = 200):

        return self.send_requests(
            method="POST",
            endpoint=MOVIES_ENDPOINT,
            data = data,
            params=params,
            headers=headers,
            expected_status=expected_status,
        )

    def get_movies_id(self, id, params = None, headers = None, expected_status = 200):

        return self.send_requests(
            method="GET",
            endpoint=MOVIES_ID_ENDPOINT.format(id = id),
            params=params,
            headers=headers,
            expected_status=expected_status
        )
    
    def delete_movies(self, id, params = None, headers = None, expected_status = 200):

        return self.send_requests(
            method="DELETE",
            endpoint=MOVIES_ID_ENDPOINT.format(id = id),
            params=params,
            headers=headers,
            expected_status=expected_status
        )

    def get_movies_reviews_id(self, id, params = None, headers = None, expected_status = 200):

        return self.send_requests(
            method="GET",
            endpoint=MOVIES_ID_REVIEWS_ENDPOINT.format(id = id),
            params=params,
            headers=headers,
            expected_status=expected_status
        )
