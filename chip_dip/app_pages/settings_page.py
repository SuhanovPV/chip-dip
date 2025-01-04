import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class SettingsPage:
    def switch_settings_checkbox(self, name):
        with allure.step(f'Switch checkbox "{name}"'):
            browser.element((AppiumBy.ID, f'ru.chipdip.mobile:id/settings_{name}_item_switch')).click()
        return self
