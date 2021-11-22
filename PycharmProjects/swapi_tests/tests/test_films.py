import requests
from utils import base_url
from utils import films
from utils import assert_attributes_type
from utils import test_film_1
from utils import execution_time

url = base_url + films


class TestFilms():
    @execution_time
    def test_response_code_of_the_films_list(self):
        response = requests.get(url)
        assert response.status_code == 200

    @execution_time
    def test_response_code_of_the_film(self):
        response = requests.get(url + '1/')
        assert response.status_code == 200

    @execution_time
    def test_the_films_list_count(self):
        response = requests.get(url)
        count_value = response.json()['count']
        count_actual = len(response.json()['results'])
        assert count_value == count_actual

    @execution_time
    def test_response_of_the_films_list_data_types(self):
        response = requests.get(url)
        films_list_results = response.json()['results']

        for film in films_list_results:
            assert_attributes_type(film, ['episode_id'], int)
            assert_attributes_type(film, ['title', 'opening_crawl', 'director', 'producer', 'release_date', 'created',
                                          'edited', 'url'], str)
            assert_attributes_type(film, ['characters', 'planets', 'starships', 'vehicles', 'species'], list)

    @execution_time
    def test_film_info_in_the_films_list_result(self):
        response = requests.get(url)
        film = response.json()['results'][0]
        for item in film:
            if item in test_film_1.keys():
                assert film[item] == test_film_1[item]

