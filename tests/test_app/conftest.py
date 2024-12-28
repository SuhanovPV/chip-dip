import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from appium import webdriver

@pytest.fixture(scope='function')
def mobile_settings(request):
    options = UiAutomator2Options().load_capabilities({
        'deviceName': 'SM-A325F',
        'app': 'D:\\education\\python\\python_testing\\chip-dip\\app-obfuscate-storeRU-release-1.14.0.apk',
        'appWaitActivity': 'ru.chipdip.mobile.activities.*',
        'appActivity': 'ru.chipdip.mobile.activities.MainActivity',
    })
    browser.config.driver = webdriver.Remote(
        'http://127.0.0.1:4723/wd/hub',
        options=options
    )
    browser.config.timeout = 7.0

@pytest.fixture(scope='function', autouse=True)
def skip_welcomescreen(mobile_settings):
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/onboarding_skip_button_text_view')).click()
    browser.element(
        (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.chipdip.mobile:id/item_geo_object_name" '
                     'and @text="Санкт-Петербург"]')
    ).click()