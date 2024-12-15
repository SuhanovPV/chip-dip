from config import password
from chip_dip.data.Users import user
from chip_dip.pages.login_form import Login


class TestAuthorization:

    def test_login_with_correct_credentials(self, logout):
        login = Login()
        login.login(user, password)
        login.should_success_auth(user)

    def test_login_with_wrong_credentials(self, logout):
        login = Login()
        login.login(user, 'hKJh8qcPet12')
        login.should_failed_auth()
