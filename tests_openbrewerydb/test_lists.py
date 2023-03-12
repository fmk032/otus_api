import pytest
import requests
import json
from data import BREW_TEST_DATA_PATH

with open(BREW_TEST_DATA_PATH, "r") as f:
    data = json.load(f) #Тест данные из breweries_test_data.json


@pytest.mark.parametrize("id", data["id"])
def test_singe_brewery(id):
    """Тест проверяет, что возвращенный brewery соответствует id.
    id's указаны в breweries_test_data.json."""
    res = requests.get(data['url'] + "/" + id)
    assert res.json()['id'] == id


@pytest.mark.parametrize("per_page", data["per_page"])
def test_list_breweries(per_page):
    """Тест проверяет, что число возвращенных на странице breweries соответствует per_page.
    per_page указаны в breweries_test_data.json."""
    res = requests.get(data['url'] + "?" + "&per_page=" + per_page)
    assert str(len(res.json())) == per_page


@pytest.mark.parametrize("per_page", data["per_page"])
@pytest.mark.parametrize("query", data["query"])
def test_search_breweries(query, per_page):
    """Тест проверяет, что все возвращенные breweries соответствуют query.
    queries и число breweries на странице указаны в breweries_test_data.json."""
    res = requests.get(data['url'] + "/search?query=" + query + "&per_page=" + per_page)
    for br in res.json():
        assert br['id'].find(query) != -1