import requests


def test_url_status(pytestconfig):
    """Принимает url & status_code через cli.
    Проверяет, что при запросе к принятому url возвращается принятый status_code"""
    res = requests.get(pytestconfig.getoption('url'))
    assert res.status_code == int(pytestconfig.getoption('status_code'))