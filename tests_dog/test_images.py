import pytest
import requests


def msg_assert(msg, breed=""):
    """Принимает ссылку, возвращенную на запрос к API, проверяет ее формат"""
    assert msg[:30 + len(breed)] == "https://images.dog.ceo/breeds/" + breed and msg[-4:] == ".jpg"


def test_random_image():
    """Проверяет формат ссылки, возвращенной на random запрос"""
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    msg_assert(r.json()["message"])


@pytest.mark.parametrize("n", (1, 5, 50))
def test_random_mutiple_images(n):
    """Проверяет формат и число ссылок, возвращенных на multiple random запрос"""
    r = requests.get("https://dog.ceo/api/breeds/image/random/" + str(n))
    msg = r.json()["message"]
    for img in msg:
        msg_assert(img)
    assert len(msg) == n


def test_breed_subbreed_random_image(url):
    """Проверяет формат ссылки, возвращенной на breed or subbreed random запрос"""
    r = requests.get(url['url'] + "/random")
    msg_assert(r.json()["message"], url['breed'])


@pytest.mark.parametrize("n", (1, 5, 50))
def test_breed_subbreed_random_multiple_images(url, n):
    """Проверяет формат и число ссылок, возвращенных на breed or subbreed multiple random запрос"""
    r = requests.get(url['url'] + "/random/" + str(n))
    msg = r.json()["message"]
    for img in msg:
        msg_assert(img, url['breed'])
    assert len(msg) == n


def test_all_breed_subbreed_images(url):
    """Проверяет формат и наличие ссылок, возвращенных на ALL breed or subbreed запрос"""
    r = requests.get(url['url'])
    msg = r.json()["message"]
    for img in msg:
        msg_assert(img, url['breed'])
    assert len(msg) != 0
