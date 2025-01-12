import allure
import pytest

from chip_dip.data.Users import user
from chip_dip.pages.login_form import Login


@allure.suite('Website')
@allure.parent_suite('Chip Dip services')
@allure.sub_suite('Authorization tests')
@allure.epic('Authorization')
@allure.story('Tests for login on site')
@pytest.mark.usefixtures('browser_settings')
class TestAuthorization:

    @allure.tag('web', 'auth', 'login')
    @allure.title('login to site with correct credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_correct_credentials(self, logout):
        login = Login()
        with allure.step('Login'):
            login.login(user.login, user.password)
        with allure.step('Check user logged in'):
            login.should_success_auth(user)

    @allure.tag('web', 'auth', 'login')
    @allure.title('login to site with wrong credentials')
    @allure.severity(allure.severity_level.MINOR)
    def test_login_with_wrong_credentials(self, logout):
        login = Login()
        with allure.step('Login'):
            login.login(user.login, 'hKJh8qcPet12')
        with allure.step('Check user logged in'):
            login.should_failed_auth()
