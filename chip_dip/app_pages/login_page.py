from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class LoginPage:
    def login(self, login, password):
        browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/edit_text_text')).first.type(login)
        browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/edit_text_text')).second.type(password)
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/progress_button_text_view')).click()
        return self