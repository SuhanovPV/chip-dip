import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class MainPage:
    @staticmethod
    def is_welcome_screen():
        with allure.step('Check is welcome screen open'):
            return browser.element(
                (AppiumBy.ID, 'ru.chipdip.mobile:id/onboarding_skip_button_text_view')
            ).matching(be.existing)

    def scip_welcome_screen(self):
        with allure.step('Skip welcome screen'):
            browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/onboarding_skip_button_text_view')).click()
        return self

    def select_region(self):
        with allure.step('Select region'):
            browser.element(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.chipdip.mobile:id/item_geo_object_name" '
                                 'and @text="Санкт-Петербург"]')
            ).click()
        return self

    def open_auth_page(self):
        with allure.step('Open login page'):
            browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_header_profile_button_text_view')).click()
            browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/authorization_info_button')).click()
        return self

    def open_page_via_side_menu(self, button_name):
        with allure.step(f'Open "{button_name}" page'):
            self.open_menu()
            browser.element((AppiumBy.ID, f'ru.chipdip.mobile:id/main_{button_name}_button')).click()
        return self

    def open_menu(self):
        with allure.step('Open menu'):
            if browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).matching(be.existing):
                browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click()
            else:
                browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_menu_button_image_view')).click()
        return self

    def should_section_be_missing(self, name):
        with allure.step(f'Check section "{name}" is missing'):
            browser.element(f'ru.chipdip.mobile:id/main_header_{name}_button_text_view').should(have.no.existing)
        return self
