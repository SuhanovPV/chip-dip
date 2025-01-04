from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class MainPage:
    @staticmethod
    def is_welcome_screen():
        return browser.element(
            (AppiumBy.ID, 'ru.chipdip.mobile:id/onboarding_skip_button_text_view')
        ).matching(be.existing)

    def scip_welcome_screen(self):
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/onboarding_skip_button_text_view')).click()
        return self

    def select_region(self):
        browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.chipdip.mobile:id/item_geo_object_name" '
                             'and @text="Санкт-Петербург"]')
        ).click()
        return self

    def open_auth_page(self):
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_header_profile_button_text_view')).click()
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/authorization_info_button')).click()
        return self

    def open_page_via_side_menu(self, button_name):
        self.open_menu()
        browser.element((AppiumBy.ID, f'ru.chipdip.mobile:id/{button_name}')).click()
        return self

    def open_menu(self):
        if browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).matching(be.existing):
            browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click()
        else:
            browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_menu_button_image_view')).click()
        return self

    def should_section_be_missing(self, name):
        browser.element(f'ru.chipdip.mobile:id/main_header_{name}_button_text_view').should(have.no.existing)
        return self
