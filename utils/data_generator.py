import random
from faker import Faker

faker = Faker()

class DataGenerator:

    @staticmethod
    def valid_data_for_create_movies():
        return {
            "name": faker.catch_phrase(),
            "imageUrl": faker.image_url(),
            "price": random.randint(100, 1000),
            "description": faker.text(max_nb_chars=250),
            "location": random.choice(["SPB", "MSK"]),
            "published": random.choice([True, False]),
            "genreId": random.randint(1, 10)
        }
        
    @staticmethod
    def min_valid_data_for_create_movies():
        return {
            "name": faker.catch_phrase(),
            "price": random.randint(100, 1000),
            "description": faker.text(max_nb_chars=250),
            "location": random.choice(["SPB", "MSK"]),
            "published": random.choice([True, False]),
            "genreId": random.randint(1, 10)
        }
    