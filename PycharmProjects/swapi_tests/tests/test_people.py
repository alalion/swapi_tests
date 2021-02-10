import requests
from utils.utils import base_url
from utils.utils import people
from utils.utils import search
from utils.utils import assert_attributes_type
from utils.test_person_1 import *

url = base_url + people


class TestPeople():

    def test_response_code_of_the_people_list_result(self):
        response = requests.get(url)
        assert response.status_code == 200

    def test_response_code_of_the_person_result(self):
        response = requests.get(url + '1/')
        assert response.status_code == 200

    def test_response_of_the_people_list_result_data_types(self):
        response = requests.get(url)
        people_list_result = response.json()['results']

        for person in people_list_result:
            assert_attributes_type(person, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color',
                                            'birth_year', 'gender', 'homeworld', 'created', 'edited', 'url'], str)
            assert_attributes_type(person, ['films', 'species', 'vehicles', 'starships'], list)

    def test_search_people(self):
        response = requests.get(url + search + 'Luke Skywalker')
        assert response.json()['results'][0]['name'] == name
        assert response.json()['results'][0]['height'] == height
        assert response.json()['results'][0]['mass'] == mass
        assert response.json()['results'][0]['hair_color'] == hair_color
        assert response.json()['results'][0]['skin_color'] == skin_color
        assert response.json()['results'][0]['eye_color'] == eye_color
        assert response.json()['results'][0]['birth_year'] == birth_year
        assert response.json()['results'][0]['gender'] == gender
        assert response.json()['results'][0]['homeworld'] == homeworld
        assert response.json()['results'][0]['films'] == films
        assert response.json()['results'][0]['species'] == species
        assert response.json()['results'][0]['vehicles'] == vehicles
        assert response.json()['results'][0]['starships'] == starships
        assert response.json()['results'][0]['created'] == created
        assert response.json()['results'][0]['edited'] == edited
        assert response.json()['results'][0]['url'] == person_url

    def test_search_people_by_partial_name(self):
        response = requests.get(url + search + 'anakin')
        assert response.json()['results'][0]['name'] == 'Anakin Skywalker'

