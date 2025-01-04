import allure
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver

from chip_dip.app_pages.login_page import LoginPage
from chip_dip.utils import path_helper
from chip_dip.app_pages.main_page import MainPage


@pytest.fixture(scope='class', autouse=True)
def mobile_settings(request):
    options = UiAutomator2Options().load_capabilities({
        'deviceName': 'SM_G990E',
        'app': path_helper.abs_path_from_project('app-obfuscate-storeRU-release-1.14.0.apk'),
        'appWaitActivity': 'ru.chipdip.mobile.activities.*',
        'appActivity': 'ru.chipdip.mobile.activities.MainActivity',
        'noRest': True
    })
    # options = UiAutomator2Options().load_capabilities({
    #     'platformName': 'android',
    #     'platformVersion': '9.0',
    #     'deviceName': 'Google Pixel 3',
    #     'app': 'bs://72afc2c8d2e6b553ea2598c1bd3c8f28baa534c4',
    #     'bstack:options': {
    #         "sessionName": "Chip-dip",
    #         "projectName": 'project',
    #         "userName": 'bsuser_1YN2Xq',
    #         "accessKey": 'GvG55x2cbZ5aBS2HBrzx'
    #     }
    # })
    browser.config.driver = webdriver.Remote(
        'http://127.0.0.1:4723/wd/hub',
        # 'http://hub.browserstack.com/wd/hub',
        options=options
    )
    browser.config.timeout = 20.0
    yield
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def skip_welcome_screen(mobile_settings):
    main_page = MainPage()
    if main_page.is_welcome_screen():
        with allure.step('Skip welcome screen'):
            main_page.scip_welcome_screen() \
                .select_region()
        with allure.step('Login'):
            main_page.open_auth_page()
            login_page = LoginPage()
            login_page.login('ssuxxarr', 'hKJh8qcP12')
