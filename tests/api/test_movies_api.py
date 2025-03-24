import random

class TestMoviesAPI:
    
    def test_get_all_movies(self, api_manager):
        '''Успешное получение списка всех фильмов'''
        response = api_manager.movies_api.get_movies()
        assert response.status_code == 200, "Получение списка фильма провалено"
        assert type(response.json()["movies"]) == list, "Получен не список"


    def test_get_filter_movies(self, api_manager):
        '''Успешное получение списка фильмов с фильтрацией по: `pageSize`, `page`, `minPrice`, `maxPrice`, `locations`, `genreId`, `createdAt`'''
        json_filter = {
            "locations" : "SPB"
        }
        response = api_manager.movies_api.get_movies(params = json_filter)
        assert response.status_code == 200, "Фильтрация провалена"

    def test_failed_get_movies(self, api_manager):
        '''Негативный тест: передача неверных параметров.'''
        json_filter = {
            "minPrice" : "-1000",
        }
        response = api_manager.movies_api.get_movies(expected_status = 400, params = json_filter)
        assert "error" in response.json(), "Ошибки нет"

    def test_post_movies_valid_data(self, api_manager, super_admin_token, valid_data_for_create_movies):
        """нужен токен super_admin"""
        '''Успешное создание фильма с валидными данными (**SUPER_ADMIN**)'''
        response = api_manager.movies_api.post_movies(data = valid_data_for_create_movies, headers = super_admin_token, expected_status = 201 )
        response = api_manager.movies_api.get_movies()
        movie_titles = [movie["name"] for movie in response.json()["movies"]]
        assert "Название фильма" in movie_titles, "Фильма нет в списке"
        assert response.status_code == 201, "Фильм не создан"

    def test_post_movies_min_valid_data(self, api_manager, super_admin_token, min_valid_data_for_create_movies):
        """нужен токен super_admin"""
        '''Успешное создание фильма с валидными данными (**SUPER_ADMIN**)'''
        response = api_manager.movies_api.post_movies(data = min_valid_data_for_create_movies, headers = super_admin_token, expected_status = 201 )
        response = api_manager.movies_api.get_movies()
        movie_titles = [movie["name"] for movie in response.json()["movies"]]
        assert "Название фильма" in movie_titles, "Фильма нет в списке"
        assert response.status_code == 201, "Фильм не создан"

    def test_falied_post_movies(self, api_manager, super_admin_token, valid_data_for_create_movies):
        """нужен токен super_admin"""
        '''Негативный тест: создание фильма с уже существующим названием (**SUPER_ADMIN**)'''
        response = api_manager.movies_api.get_movies()
        movie_titles = [movie["name"] for movie in response.json()["movies"]]
        valid_data_for_create_movies["name"] = movie_titles[0]
        response = api_manager.movies_api.post_movies(data = valid_data_for_create_movies, headers = super_admin_token, expected_status = 409 )
        assert response.status_code == 409, "Фильм не создан"

    def test_get_movies_id(self, api_manager):
        '''Успешное получение фильма по валидному ID'''
        response = api_manager.movies_api.get_movies()
        movie_id = [movie["id"] for movie in response.json()["movies"]][0]
        response = api_manager.movies_api.get_movies_id(movie_id)
        assert response.status_code == 200, "Фильм не найден"

    def test_failed_get_movies_id(self, api_manager):
        '''Негативный тест: получение фильма с несуществующим ID'''
        response = api_manager.movies_api.get_movies()
        not_movie_id = max([movie["id"] for movie in response.json()["movies"]]) + 1000
        response = api_manager.movies_api.get_movies_id(not_movie_id, expected_status = 404)
        assert response.status_code == 404, "Фильм найден"

    def test_delete_movies_id(self, api_manager, super_admin_token):
        """нужен токен super_admin"""
        #фикстура создания любого фильма
        '''Успешное удаление фильма (**SUPER_ADMIN**)'''
        response = api_manager.movies_api.get_movies()
        movie_id = [movie["id"] for movie in response.json()["movies"]][0]
        response = api_manager.movies_api.delete_movies(movie_id, headears = super_admin_token)
        assert response.status_code == 200, "Фильм не удален"
        response = api_manager.movies_api.get_movies()
        assert movie_id not in [movie["id"] for movie in response.json()["movies"]], "Фильм найден"
        
    def test_failed_delete_movies_id(self, api_manager, super_admin_token):
        """нужен токен super_admin"""
        '''Негативный тест: удаление несуществующего фильма. (**SUPER_ADMIN**)'''
        response = api_manager.movies_api.get_movies()
        not_movie_id = max([movie["id"] for movie in response.json()["movies"]]) + 100
        response = api_manager.movies_api.delete_movies(not_movie_id, headears = super_admin_token)
        assert response.status_code == 404, "Ошибка удаления фильма"
        
    def test_get_movies_reviews_id(self, api_manager):
        '''Успешное получение всех отзывов для фильма'''
        response = api_manager.movies_api.get_movies()
        movie_id = random.choice([movie["id"] for movie in response.json()["movies"]])
        response = api_manager.movies_api.get_movies_reviews_id(movie_id)
        assert type(response.json()) == list, "Нет списка отзывов"
        assert response.status_code == 200, "Фильм не найден"
