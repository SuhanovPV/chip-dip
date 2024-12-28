import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_auth():
    with allure.step("Authorization"):
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_header_profile_button_text_view')).click()
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/authorization_info_button')).click()
        browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/edit_text_text')).first.type('ssuxxarr')
        browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/edit_text_text')).second.type('hKJh8qcP12')
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/progress_button_text_view')).click()
    with allure.step("Check"):
        browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/profile_personal_data_button_text_view')).click()
        browser.all((AppiumBy.ID, 'ru.chipdip.mobile:id/edit_text_text')).should(have.exact_texts(
            'ssuxxarr',
            'Павел',
            'Суханов',
            'Викторович',
            'ssuxxarr@mail.ru',
            '+79030266669',
        ))

    with allure.step('Teardown'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click()

def test_add_product_to_cart():
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_header_catalog_button_text_view')).click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/search_bar_input_edit_text')).click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/search_bar_input_edit_text')).type('HMC8038LP4CETR')
    browser.all(
        (AppiumBy.ID, 'ru.chipdip.mobile:id/item_catalog_text_label_text_view')
    ).first.should(have.text('HMC8038LP4CETR'))
    browser.all(
        (AppiumBy.ID, 'ru.chipdip.mobile:id/item_catalog_text_label_text_view')
    ).first.click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/progress_button_text_view')).click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/floating_cart_button')).click()
    browser.element(
        (AppiumBy.ID, 'ru.chipdip.mobile:id/item_cart_product_name_label_text_view')
    ).should(have.text('HMC8038LP4CETR'))


def test_settings():
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_header_settings_button_text_view')).click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/settings_favorites_item_switch')).click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/settings_information_item_switch')).click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/settings_information_item_switch')).click()
    browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click()
    browser.element((AppiumBy.ID, 'ru.chipdip.mobile:id/main_home_button')).click()
    browser.element('ru.chipdip.mobile:id/main_header_profile_button_text_view').should(have.exact_texts('Профиль'))
    browser.element('ru.chipdip.mobile:id/main_header_orders_button_text_view').should(have.exact_texts('Заказы'))
    browser.element('ru.chipdip.mobile:id/main_header_favorites_button_text_view').should(have.no.existing)
    browser.element('ru.chipdip.mobile:id/main_header_info_button_text_view').should(have.no.existing)











