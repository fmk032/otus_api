
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="request url"
    )

    parser.addoption(
        "--status_code",
        default="200",
        help="response status code"
    )
