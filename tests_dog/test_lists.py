import pytest
import requests
from jsonschema import validate
from tests_dog import conftest


def test_breeds_list_status_code(breeds_list):
    assert breeds_list.status_code == 200


def test_breeds_list_json_schema(breeds_list):
    schema = {
        "status": "string",
        "message": {},
        "required": ["status", "message"]
            }
    validate(instance=breeds_list.json(), schema=schema)


def test_breeds_list_json_status(breeds_list):
    j = breeds_list.json()
    assert j['status'] == 'success' and len(j['message']) != 0


@pytest.mark.parametrize("subbreed", conftest.subbreeds)
def test_subbreeds_list(subbreed):
    """Проверяет, что ответ на запрос списка subbredds for a breed включает переданную subbreed"""
    breed = subbreed.split("/")[0]
    sbreed = subbreed.split("/")[1]
    r = requests.get("https://dog.ceo/api/breed/" + breed +"/list")
    msg = r.json()['message']
    assert msg.count(sbreed) == 1
