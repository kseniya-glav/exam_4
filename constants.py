BASE_URL = "https://api.dev-cinescope.coconutqa.ru/"
AUTH_URL = "https://auth.dev-cinescope.coconutqa.ru/"

BASE_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

MOVIES_ENDPOINT = "/movies"
MOVIES_ID_ENDPOINT = "/movies/{id}"
MOVIES_ID_REVIEWS_ENDPOINT = "/movies/{id}/reviews"
GENRES_ENDPOINT = "/genres"
GENRES_ID_ENDPOINT = "/genres/{id}"

REGISTER_ENDPOINT = "/register"
LOGIN_ENDPOINT = "/login"

SUPER_ADMIN = {
    "email": "api1@gmail.com",
    "password": "asdqwe123Q"
}
