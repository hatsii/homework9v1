import pytest
from selene import browser
from pathlib import Path


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 3

    yield

    browser.quit()


@pytest.fixture
def open_registration_page():
    browser.open('/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


@pytest.fixture
def resources_file_path():
    def get_path(filename):
        return str((Path(__file__).parent.parent / 'resources' / filename).absolute())

    return get_path