from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT, AUTH_URL
from custom_requester.custom_requester import CustomRequester

class AuthAPI(CustomRequester):
    """Класс для работы с аутентификацией."""
    def __init__(self, session):
        super().__init__(base_url = AUTH_URL)
        self.session = session

    def register_user(self, user_data, expected_status = 201):
        return self.send_requests(
            method="POST",
            endpoint=REGISTER_ENDPOINT,
            data=user_data,
            expected_status=expected_status
        )
    
    def login_user(self, login_data, expected_status = 200):
        return self.send_requests(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            json=login_data,
            expected_status=expected_status
        )
    
    def authenticate(self, login_data):
        response = self.login_user(login_data).json()
        if "accessToken" not in response:
            raise KeyError("token is missing")
        token = response["accessToken"]
        self._update_session_headers(self.session, {"Authorization": f"Bearer {token}"})
