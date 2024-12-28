import allure
import pytest
from chip_dip.data.Users import user
from chip_dip.pages.cart_page import CartPage
from chip_dip.pages.login_form import Login
from chip_dip.utils import allure_attach
from config import password
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='class', autouse=True)
def browser_set():
    with allure.step("Setup. Set browser"):
        options = webdriver.FirefoxOptions()
        browser.config.driver_options = options
        browser.config.window_width = '1920'
        browser.config.window_height = '1080'
        browser.config.base_url = 'https://www.chipdip.ru'
        browser.config.timeout = 5.0

    yield
    allure_attach.page_source(browser)
    allure_attach.screenshot(browser)
    browser.quit()


@pytest.fixture(scope='class')
def login():
    browser.open('/')
    login = Login()
    login.login_if_no_auth(user, password)


@pytest.fixture(scope='function')
def logout():
    browser.open('/')
    login = Login()
    login.logout_if_login()

@pytest.fixture(scope='function')
def clear_cart():
    cart = CartPage()
    cart.clear_if_not_empty()

