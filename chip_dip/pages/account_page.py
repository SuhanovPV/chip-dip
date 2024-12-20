import allure
from selene import browser, have


class AccountPage:
    @staticmethod
    def _open():
        with allure.step('Open accoun page'):
            browser.open('/account')

    @staticmethod
    def _logout():
        with allure.step('Click logout'):
            browser.element('[href="/account/logoff"]').click()

    @staticmethod
    def _should_logout():
        with allure.step('Check user logged out'):
            browser.element('[href = "/account"]').should(have.exact_text('Вход'))

    def logout(self):
        with allure.step('Logout'):
            self._open()
            self._logout()
            self._should_logout()