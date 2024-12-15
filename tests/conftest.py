import pytest
from chip_dip.data.Users import user
from chip_dip.pages.login_form import Login
from config import password
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='class', autouse=True)
def browser_set():
    options = webdriver.FirefoxOptions()
    browser.config.driver_options = options
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.base_url = 'https://www.chipdip.ru'
    browser.config.timeout = 7.0

    yield

    browser.quit()


@pytest.fixture(scope='class')
def login():
    browser.open('/')
    login = Login()
    login.login_if_not_logged_with_required_user(user, password)
    browser.open('/')


@pytest.fixture(scope='function')
def logout():
    browser.open('/')
    login = Login()
    login.logout_if_login()
    browser.open('/')
