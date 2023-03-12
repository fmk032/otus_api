import pytest
import requests


@pytest.fixture()
def breeds_list():
    yield requests.get("https://dog.ceo/api/breeds/list/all")

# Breeds & sub-breeds to test
breeds = [
    "doberman",
    "terrier"
    ]
subbreeds = [
    "collie/border",
    "terrier/fox"
    ]


@pytest.fixture(params=breeds+subbreeds)
def url(request):
    """Фикструра принимает параметры breeds+subbreeds,
    возвращает словарь с url запроса и принятыми параметрами"""
    yield {
            "url": "https://dog.ceo/api/breed/" + request.param + "/images",
            "breed": request.param.replace("/", "-")
            }
