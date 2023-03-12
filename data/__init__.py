import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


BREW_TEST_DATA_PATH = get_path(filename="breweries_test_data.json")
JSONPH_TEST_DATA_PATH = get_path(filename="jsonplaceholder_test_data.json")
