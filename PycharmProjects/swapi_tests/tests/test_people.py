import requests
from utils import base_url, execution_time
from utils import people
from utils import search
from utils import assert_attributes_type
from utils import test_person_1

url = base_url + people


class TestPeople():
    @execution_time
    def test_response_code_of_the_people_list_result(self):
        response = requests.get(url)
        assert response.status_code == 200

    @execution_time
    def test_response_code_of_the_person_result(self):
        response = requests.get(url + '1/')
        assert response.status_code == 200

    @execution_time
    def test_response_of_the_people_list_result_data_types(self):
        response = requests.get(url)
        people_list_result = response.json()['results']

        for person in people_list_result:
            assert_attributes_type(person, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color',
                                            'birth_year', 'gender', 'homeworld', 'created', 'edited', 'url'], str)
            assert_attributes_type(person, ['films', 'species', 'vehicles', 'starships'], list)

    @execution_time
    def test_person_info_in_the_people_list_result(self):
        response = requests.get(url)
        person = response.json()['results'][0]
        self.assertDictEqual(test_person_1, person)

    @execution_time
    def test_person_info_on_person_url(self):
        response = requests.get(test_person_1['url'])
        self.assertDictEqual(test_person_1, response.json())

    @execution_time
    def test_search_people(self):
        response = requests.get(url + search + 'Luke Skywalker')
        found_result = response.json()['results'][0]
        self.assertDictEqual(test_person_1, found_result)

    @execution_time
    def test_search_people_by_partial_name(self):
        response = requests.get(url + search + 'anakin')
        assert response.json()['results'][0]['name'] == 'Anakin Skywalker'
