import pytest
import requests
import json
from data import JSONPH_TEST_DATA_PATH

with open(JSONPH_TEST_DATA_PATH, "r") as f:
    data = json.load(f) #Тест данные из jsonplaceholder_test_data.json


@pytest.mark.parametrize('id', data['id'])
def test_get_resource(id):
    """Тест проверяет, что возвращенная запись соответствует id.
    id's указаны в jsonplaceholder_test_data.json."""
    res = requests.get(data['url'] + '/' + str(id))
    assert res.json()['id'] == id


def test_get_resource_list():
    """Тест проверяет, что возвращенный список всех записей содержит 100 записей."""
    res = requests.get(data['url'])
    assert len(res.json()) == 100


@pytest.mark.parametrize('resource', data['resources_to_create'])
def test_create_resource(resource):
    """Тест проверяет, что ответ на post запрос на создание ресурса соответствует полям ресурса.
    resources указаны в jsonplaceholder_test_data.json."""
    res = requests.post(data['url'], resource)
    resource['id'] = 101
    assert res.json() == resource


@pytest.mark.parametrize('resource', data['resources_to_create'])
@pytest.mark.parametrize('id', data['id'])
def test_update_resource(resource, id):
    """Тест проверяет, что ответ на put запрос на обновление ресурса соответствует полям ресурса и id.
        resources & id's указаны в jsonplaceholder_test_data.json."""
    resource['id'] = id
    res = requests.put(data['url'] + '/' + str(id), resource)
    assert res.json() == resource


@pytest.mark.parametrize('patch', data['patch'])
@pytest.mark.parametrize('id', data['id'])
def test_patch_resource(patch, id):
    """Тест проверяет, что ответ на patch запрос соответствует patch & id.
    patches & id's указаны в jsonplaceholder_test_data.json."""
    res = requests.patch(data['url'] + '/' + str(id), patch)
    assert res.json()[list(patch.keys())[0]] == list(patch.values())[0]


def test_delete_resource():
    res = requests.delete(data['url'] + '/1')
    assert res.status_code == 200