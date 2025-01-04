import allure

from chip_dip.app_pages.cart_page import CartPage
from chip_dip.app_pages.catalog_page import CatalogPage
from chip_dip.app_pages.main_page import MainPage
from chip_dip.app_pages.settings_page import SettingsPage


class TestApp:
    def test_add_product_to_cart(self):
        product = 'HMC8038LP4CETR'
        main_page = MainPage()
        cart_page = CartPage()
        catalog_page = CatalogPage()
        with allure.step('Clear cart if not empty'):
           cart_page.clear_cart_if_not_empty()
        with allure.step(f'Add product "{product}" to cart'):
            main_page.open_page_via_side_menu('catalog')
            catalog_page.search_product_in_catalog(product) \
                .add_founded_product_to_cart() \
                .back_to_catalog_from_search()
            main_page.open_page_via_side_menu('cart')

        with allure.step(f'Check product "{product}" in cart'):
            cart_page.should_product_be_in_cart(product)

    def test_clear_cart(self):
        product = 'FSCQ0765RTYDTU'
        main_page = MainPage()
        cart_page = CartPage()
        catalog_page = CatalogPage()
        with allure.step(f'Add product "{product}" to cart'):
            main_page.open_page_via_side_menu('catalog')
            catalog_page.search_product_in_catalog(product) \
                .add_founded_product_to_cart() \
                .back_to_catalog_from_search()
        with allure.step('Clear cart'):
            main_page.open_page_via_side_menu('cart')
            cart_page.clear_cart()

        with allure.step('Check cart is empty'):
            cart_page.should_cart_be_empty()


    def test_display_of_sections_on_main_page(self):
        main_page = MainPage()
        settings_page = SettingsPage()
        with allure.step('Set display of sections in settings'):
                main_page.open_page_via_side_menu('settings')
                settings_page.switch_settings_checkbox('orders') \
                    .switch_settings_checkbox('favorites') \
                    .switch_settings_checkbox('information')
                main_page.open_page_via_side_menu('home')

        with allure.step('Check switched off sections not displayed'):
            main_page.should_section_be_missing('orders') \
                .should_section_be_missing('favorites') \
                .should_section_be_missing('info')
