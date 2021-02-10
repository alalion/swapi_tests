# API URL

base_url = 'https://swapi.dev/api/'
people = 'people/'
films = 'films/3/'
planets = 'planets/1/'
starships = 'starships/1/'
search = '?search='

# Verify data type


def assert_attributes_type(_dict, key_list, _type):
    for key in key_list:
        assert isinstance(_dict[key], _type)
