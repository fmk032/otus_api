import pytest
import requests
import json
from data import BREW_TEST_DATA_PATH

with open(BREW_TEST_DATA_PATH, "r") as f:
    data = json.load(f) #Тест данные из breweries_test_data.json

def ld(fl):
    """Генератор фильтров из списка filters в breweries_test_data.json"""
    for n in fl:
        for m in n['values']:
            yield {'filter': n['filter'], 'key': n['key'], 'value': m}


total = int(requests.get(data['url'] + "/meta").json()['total'])

@pytest.mark.parametrize("per_page", data["per_page"])
@pytest.mark.parametrize("item", ld(data['filters']))
def test_breweries_filter(item, per_page):
    """Тест проверяет, что все возвращенные breweries соответствуют фильтру.
    Фильтры и число breweries на странице указаны в breweries_test_data.json."""
    print(item) #Выводит примененный фильтр для наглядности
    res = requests.get(data['url'] + "?" + item['filter'] + "=" + item['value'] + "&per_page=" + per_page)
    for br in res.json():
        assert br[item['key']].find(item['value']) != -1


@pytest.mark.parametrize("item1", ld(data['filters']))
@pytest.mark.parametrize("item2", ld(data['filters']))
def test_breweries_2_filters(item1, item2):
    """Тест проверяет, что все возвращенные breweries соответствуют двум фильтрам.
    Фильтры указаны в breweries_test_data.json."""
    if item1["filter"] == item2["filter"]:
        pytest.skip('The same filter')
    res = requests.get(data['url'] + "?" + item1["filter"] + "=" + item1['value'] + "&" + item2["filter"] + "=" + item2['value'] + "&per_page=3")
    print(item1) #Выводит примененный фильтр 1 для наглядности
    print(item2) #Выводит примененный фильтр 2 для наглядности
    for br in res.json():
        assert br[item1['key']].find(item1['value']) != -1 and br[item2['key']].find(item2['value']) != -1


def test_meta_all():
    """Тест проверяет, что все возвращенные c фильтром мета данные больше нуля"""
    res = requests.get(data['url'] + "/meta")
    assert total > 0
    assert int(res.json()['page']) > 0
    assert int(res.json()['per_page']) > 0


@pytest.mark.parametrize("item", ld(data['filters']))
def test_meta_filter(item):
    """Тест проверяет, что все возвращенные c фильтром мета данные больше нуля и total е выше общего числа записей.
        Фильтры указаны в breweries_test_data.json."""
    print(item) #Выводит примененный фильтр для наглядности
    res = requests.get(data['url'] + "/meta?" + item['filter'] + "=" + item['value'])
    assert int(res.json()['total']) > 0 and int(res.json()['total']) < total
    assert int(res.json()['page']) > 0
    assert int(res.json()['per_page']) > 0
