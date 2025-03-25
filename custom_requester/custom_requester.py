import json
import requests
import logging
import os

class CustomRequester:

    def __init__(self, base_url, headers = None):
        self.base_url = base_url
        self.headers = (headers or {})
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def send_requests(self, method, endpoint, expected_status = 200, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        self.log_request_response(response) 
        if response.status_code not in (expected_status if type(expected_status) == list else [expected_status]):
            raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")
        return response

    def _update_session_headers(self, session, headers):
        self.headers.update(headers)
        session.headers.update(self.headers)

    def log_request_response(self, response):
        try:
            request = response.request
            headers = "\n".join([f"-header: {header}: {value}" for header, value in request.headers.items()])
            if getattr(request, 'params', None):
                params = "\n".join([f"-param: {param}: {value}" for param, value in request.params.items()])
            else:
                params = f"-param: {None}"
            response_data = response.text
            try:
                response_data = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
            except json.JSONDecodeError:
                pass

            GREEN = '\033[32m'
            RED = '\033[31m'
            RESET = '\033[0m'
            self.logger.info(f"\n{'=' * 40} REQUEST {'=' * 40}")
            self.logger.info(
                f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}\n"
                f"-url: {request.url} \n"
                f"-method: {request.method} \n"
                f"{headers} \n"
                f"{params} \n"
            )
            self.logger.info(f"\n{'=' * 40} RESPONSE {'=' * 40}")
            self.logger.info(
                f"status code: {GREEN if response.ok else RED}{response.status_code}{RESET}\n"
                f"data: {response_data}\n"
            )
            self.logger.info(f"{'=' * 80}\n")
        except Exception as e:
            self.logger.error(f"\nLoging failed: {type(e)} - {e}")