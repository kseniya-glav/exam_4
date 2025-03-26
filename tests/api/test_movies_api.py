import random

class TestMoviesAPI:
    
    def test_get_all_movies(self, api_manager):
        """Успешное получение списка всех фильмов"""
        data = api_manager.movies_api.get_movies().json()
        assert data["pageSize"] == len(data["movies"]), "Списка фильмов нет"

    def test_get_filter_movies(self, api_manager):
        """Успешное получение списка фильмов с фильтрацией по `locations`"""
        json_filter = {
            "locations" : "SPB"
            }
        data = api_manager.movies_api.get_movies(params = json_filter).json()
        assert len([movie["location"] for movie in data["movies"] if movie["location"]=="SPB"]) == len(data["movies"])

    def test_failed_get_movies(self, api_manager):
        """Негативный тест: передача неверных параметров"""
        json_filter = {
            "minPrice" : "-1000"
            }
        response = api_manager.movies_api.get_movies(expected_status = 400, params = json_filter)
        assert "error" in response.json(), "Ошибки нет"

    def test_post_movies_valid_data(self, admin, new_movies):
        """Успешное создание фильма с валидными данными (**SUPER_ADMIN**)"""
        response = admin.movies_api.post_movies(json = new_movies)
        id_create_movie = response.json()["id"]
        response = admin.movies_api.get_movies_id(id_create_movie)
        assert response.json()["id"] == id_create_movie, "Фильма нет в списке"

    def test_post_movies_min_valid_data(self, admin, new_movies_min):
        """Успешное создание фильма с валидными данными (**SUPER_ADMIN**)"""
        response = admin.movies_api.post_movies(json = new_movies_min)
        id_create_movie = response.json()["id"]
        response = admin.movies_api.get_movies_id(id_create_movie)
        assert response.json()["id"] == id_create_movie, "Фильма нет в списке"

    def test_falied_post_movies(self, admin, new_movies):
        """Негативный тест: создание фильма с уже существующим названием (**SUPER_ADMIN**)"""
        response = admin.movies_api.get_movies()
        new_movies["name"] = response.json()["movies"][0]["name"]
        response = admin.movies_api.post_movies(json = new_movies, expected_status = 409)
        assert "error" in response.json(), "Ошибки нет"

    def test_get_movies_id(self, api_manager):
        """Успешное получение фильма по валидному ID"""
        response = api_manager.movies_api.get_movies()
        movie_id = [movie["id"] for movie in response.json()["movies"]][0]
        response = api_manager.movies_api.get_movies_id(movie_id)
        assert response.json()["id"] == movie_id, "Фильм не тот"

    def test_failed_get_movies_id(self, api_manager):
        """Негативный тест: получение фильма с несуществующим ID"""
        response = api_manager.movies_api.get_movies()
        not_movie_id = max([movie["id"] for movie in response.json()["movies"]]) + 1000
        response = api_manager.movies_api.get_movies_id(not_movie_id, expected_status = 404)
        assert "error" in response.json(), "Ошибки нет"

    def test_delete_movies_id(self, admin, create_movies):
        """Успешное удаление фильма (**SUPER_ADMIN**)"""
        movie_id = create_movies["id"]
        response = admin.movies_api.delete_movies(movie_id)
        assert response.status_code == 200, 'Фильм не удален'
        response = admin.movies_api.get_movies_id(movie_id, expected_status = 404)
        assert "error" in response.json(), "Ошибки нет"
        
    def test_failed_delete_movies_id(self, admin):
        """Негативный тест: удаление несуществующего фильма. (**SUPER_ADMIN**)"""
        response = admin.movies_api.get_movies()
        not_movie_id = max([movie["id"] for movie in response.json()["movies"]]) + 1000
        response = admin.movies_api.delete_movies(not_movie_id, expected_status = 404)
        assert "error" in response.json(), "Ошибки нет"
        
    def test_get_movies_reviews_id(self, api_manager):
        """Успешное получение всех отзывов для фильма"""
        response = api_manager.movies_api.get_movies()
        movie_id = random.choice([movie["id"] for movie in response.json()["movies"]])
        data = api_manager.movies_api.get_movies_reviews_id(movie_id).json()
        assert data[0]["user"]["fullName"] if data else type(data) == list, "Список отзывов отсутствует"
