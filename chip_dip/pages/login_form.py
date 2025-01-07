import allure
from selene import browser, have
from chip_dip.data.Users import User
from chip_dip.pages.account_page import AccountPage


class Login:
    @staticmethod
    def _open():
        with allure.step('Open login page'):
            browser.open('/account/logon')

    @staticmethod
    def _fill_login(login):
        with allure.step(f'Fill login field: "{login}"'):
            browser.element('#logonform input[name="login"]').type(login)

    @staticmethod
    def _fill_password(password):
        with allure.step('Fill password field'):
            browser.element('#logonform input[name="pwd"]').type(password)

    @staticmethod
    def _submit():
        with allure.step('Submit authorization form'):
            browser.element('#logonform button[type="submit"]').click()

    def login(self, login: str, password: str):
        with allure.step(f'Authorization with login "{login}"'):
            self._open()
            self._fill_login(login)
            self._fill_password(password)
            self._submit()

    @staticmethod
    def should_success_auth(user: User):
        with allure.step('Check success authorization'):
            browser.element('.header__main-link[href="/account"]').should(
                have.exact_text(f'{user.first_name} {user.last_name}'))

    @staticmethod
    def should_failed_auth():
        browser.element('.form__globalerror').should(
            have.exact_text('Неверно указан логин или пароль, попробуйте еще раз'))

    def login_if_no_auth(self, user: User):
        with allure.step('Login if not logged in before'):
            element = browser.all('.header__main-links a').first
            if element.matching(have.exact_text('Вход')):
                with allure.step('Open auth form'):
                    element.click()
                self._fill_login(user.login)
                self._fill_password(user.password)
                self._submit()
                self.should_success_auth(user)

    @staticmethod
    def logout_if_login():
        with allure.step('Logout if not logged out before'):
            element = browser.all('.header__main-links a').first
            if not element.matching(have.exact_text('Вход')):
                account = AccountPage()
                account.logout()
