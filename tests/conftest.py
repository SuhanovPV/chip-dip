import allure

import config
import pytest
from selene import browser
from chip_dip.pages.cart_page import CartPage
from chip_dip.pages.login_form import Login
from chip_dip.app_pages.main_page import MainPage
from chip_dip.app_pages.login_page import LoginPage
from chip_dip.data.Users import user
from chip_dip.utils import allure_attach


def pytest_addoption(parser):
    parser.addoption(
        '--location',
        default='remote',
        help='--location: local, remote'
    )
    parser.addoption(
        '--service',
        default='web',
        help='--service: web, app'
    )


@pytest.fixture(scope='class', autouse=True)
def browser_settings(request):
    service = request.config.getoption('--service')
    location = request.config.getoption('--location')

    if service == 'web':
        config.set_browser(location)
    elif service == 'app':
        config.set_mobile(location)
    else:
        raise KeyError

    yield service
    session_id = browser.driver.session_id
    allure_attach.screenshot(browser)
    allure_attach.page_source(browser, service)

    browser.quit()

    if location == 'remote':
        allure_attach.video(service, session_id)


@pytest.fixture()
def mark_skip_app_test(request):
    if request.config.getoption('--service') == 'web':
        pytest.skip('This test for application')


@pytest.fixture()
def mark_skip_web_test(request):
    if request.config.getoption('--service') == 'app':
        pytest.skip('This test for web')


@pytest.fixture()
def login_if_not_auth():
    browser.open('/')
    login = Login()
    login.login_if_no_auth(user)


@pytest.fixture(scope='function')
def logout():
    browser.open('/')
    login = Login()
    login.logout_if_login()


@pytest.fixture(scope='function')
def clear_cart(login_if_not_auth):
    cart = CartPage()
    cart.clear_if_not_empty()


@pytest.fixture(scope='function')
def skip_welcome_screen():
    main_page = MainPage()
    if main_page.is_welcome_screen():
        with allure.step('Skip welcome screen'):
            main_page.scip_welcome_screen() \
                .select_region()
        with allure.step('Login'):
            main_page.open_auth_page()
            login_page = LoginPage()
            login_page.login(user.login, user.password)
