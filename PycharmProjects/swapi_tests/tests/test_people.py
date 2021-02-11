import requests
from utils.utils import base_url
from utils.utils import people
from utils.utils import search
from utils.utils import assert_attributes_type
from utils.utils import test_person_1

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

    def test_person_info_in_the_people_list_result(self):
        response = requests.get(url)
        assert response.json()['results'][0]['name'] == test_person_1['name']
        assert response.json()['results'][0]['height'] == test_person_1['height']
        assert response.json()['results'][0]['mass'] == test_person_1['mass']
        assert response.json()['results'][0]['hair_color'] == test_person_1['hair_color']
        assert response.json()['results'][0]['skin_color'] == test_person_1['skin_color']
        assert response.json()['results'][0]['eye_color'] == test_person_1['eye_color']
        assert response.json()['results'][0]['birth_year'] == test_person_1['birth_year']
        assert response.json()['results'][0]['gender'] == test_person_1['gender']
        assert response.json()['results'][0]['homeworld'] == test_person_1['homeworld']
        assert response.json()['results'][0]['films'] == test_person_1['films']
        assert response.json()['results'][0]['species'] == test_person_1['species']
        assert response.json()['results'][0]['vehicles'] == test_person_1['vehicles']
        assert response.json()['results'][0]['starships'] == test_person_1['starships']
        assert response.json()['results'][0]['created'] == test_person_1['created']
        assert response.json()['results'][0]['edited'] == test_person_1['edited']
        assert response.json()['results'][0]['url'] == test_person_1['person_url']

    def test_person_info_on_person_url(self):
        response = requests.get(test_person_1['person_url'])
        assert response.json()['name'] == test_person_1['name']
        assert response.json()['height'] == test_person_1['height']
        assert response.json()['mass'] == test_person_1['mass']
        assert response.json()['hair_color'] == test_person_1['hair_color']
        assert response.json()['skin_color'] == test_person_1['skin_color']
        assert response.json()['eye_color'] == test_person_1['eye_color']
        assert response.json()['birth_year'] == test_person_1['birth_year']
        assert response.json()['gender'] == test_person_1['gender']
        assert response.json()['homeworld'] == test_person_1['homeworld']
        assert response.json()['films'] == test_person_1['films']
        assert response.json()['species'] == test_person_1['species']
        assert response.json()['vehicles'] == test_person_1['vehicles']
        assert response.json()['starships'] == test_person_1['starships']
        assert response.json()['created'] == test_person_1['created']
        assert response.json()['edited'] == test_person_1['edited']
        assert response.json()['url'] == test_person_1['person_url']

    def test_search_people(self):
        response = requests.get(url + search + 'Luke Skywalker')
        assert response.json()['results'][0]['name'] == test_person_1['name']
        assert response.json()['results'][0]['height'] == test_person_1['height']
        assert response.json()['results'][0]['mass'] == test_person_1['mass']
        assert response.json()['results'][0]['hair_color'] == test_person_1['hair_color']
        assert response.json()['results'][0]['skin_color'] == test_person_1['skin_color']
        assert response.json()['results'][0]['eye_color'] == test_person_1['eye_color']
        assert response.json()['results'][0]['birth_year'] == test_person_1['birth_year']
        assert response.json()['results'][0]['gender'] == test_person_1['gender']
        assert response.json()['results'][0]['homeworld'] == test_person_1['homeworld']
        assert response.json()['results'][0]['films'] == test_person_1['films']
        assert response.json()['results'][0]['species'] == test_person_1['species']
        assert response.json()['results'][0]['vehicles'] == test_person_1['vehicles']
        assert response.json()['results'][0]['starships'] == test_person_1['starships']
        assert response.json()['results'][0]['created'] == test_person_1['created']
        assert response.json()['results'][0]['edited'] == test_person_1['edited']
        assert response.json()['results'][0]['url'] == test_person_1['person_url']

    def test_search_people_by_partial_name(self):
        response = requests.get(url + search + 'anakin')
        assert response.json()['results'][0]['name'] == 'Anakin Skywalker'

