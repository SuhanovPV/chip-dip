import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class LoginPage:
    def login(self, login, password):
        with allure.step('Type login to input field'):
            browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/edit_text_text')).first.type(login)
        with allure.step('Type password to input field'):
            browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/edit_text_text')).second.type(password)
        with allure.step('Click login button'):
            browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/progress_button_text_view')).click()
        return self