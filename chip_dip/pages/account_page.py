from selene import browser, have


class AccountPage:
    @staticmethod
    def _open():
        browser.open('/account')

    @staticmethod
    def _logout():
        browser.element('[href="/account/logoff"]').click()

    @staticmethod
    def _should_logout():
        browser.element('[href = "/account"]').should(have.exact_text('Вход'))

    def logout(self):
        self._open()
        self._logout()
        self._should_logout()