from selene import browser, have
from chip_dip.data.Users import User
from chip_dip.pages.account_page import AccountPage


class Login:
    @staticmethod
    def _open():
        browser.open('/account/logon')

    @staticmethod
    def _fill_login(login):
        browser.element('#logonform input[name="login"]').type(login)

    @staticmethod
    def _fill_password(password):
        browser.element('#logonform input[name="pwd"]').type(password)

    @staticmethod
    def _submit():
        browser.element('#logonform button[type="submit"]').click()

    def login(self, user: User, password: str):
        self._open()
        self._fill_login(user.login)
        self._fill_password(password)
        self._submit()

    @staticmethod
    def should_success_auth(user: User):
        browser.element('.header__main-link[href="/account"]').should(
            have.exact_text(f'{user.first_name} {user.last_name}'))

    @staticmethod
    def should_failed_auth():
        browser.element('.form__globalerror').should(
            have.exact_text('Неверно указан логин или пароль, попробуйте еще раз'))

    def login_if_not_logged_with_required_user(self, user: User, password: str):
        element = browser.all('.header__main-links a').first
        if not  element.matching(have.exact_text(f'{user.first_name} {user.last_name}')):
            if not element.matching(have.exact_text('Вход')):
                account = AccountPage()
                account.logout()
            self.login(user, password)

    @staticmethod
    def logout_if_login():
        element = browser.all('.header__main-links a').first
        if not element.matching(have.exact_text('Вход')):
            account = AccountPage()
            account.logout()

