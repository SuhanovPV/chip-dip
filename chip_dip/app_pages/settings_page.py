from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class SettingsPage:
    def switch_settings_checkbox(self, name):
        browser.element((AppiumBy.ID, f'ru.chipdip.mobile:id/settings_{name}_item_switch')).click()
        return self
