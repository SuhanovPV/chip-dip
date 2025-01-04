from chip_dip.app_pages.cart_page import CartPage
from chip_dip.app_pages.catalog_page import CatalogPage
from chip_dip.app_pages.main_page import MainPage
from chip_dip.app_pages.settings_page import SettingsPage


class TestApp:
    def test_add_product_to_cart(self):
        main_page = MainPage()
        cart_page = CartPage()
        catalog_page = CatalogPage()

        cart_page.clear_cart_if_not_empty()
        main_page.open_page_via_side_menu('main_catalog_button')
        catalog_page.search_product_in_catalog('HMC8038LP4CETR') \
            .add_founded_product_to_cart() \
            .back_to_catalog_from_search()
        main_page.open_page_via_side_menu('main_cart_button')

        cart_page.should_product_be_in_cart('HMC8038LP4CETR')

    def test_clear_cart(self):
        main_page = MainPage()
        cart_page = CartPage()
        catalog_page = CatalogPage()
        main_page.open_page_via_side_menu('main_catalog_button')
        catalog_page.search_product_in_catalog('FSCQ0765RTYDTU') \
            .add_founded_product_to_cart() \
            .back_to_catalog_from_search()
        main_page.open_page_via_side_menu('main_cart_button')
        cart_page.clear_cart()

        cart_page.should_cart_be_empty()


    def test_set_sections_on_main_page(self):
        main_page = MainPage()
        settings_page = SettingsPage()
        main_page.open_page_via_side_menu('main_settings_button')
        settings_page.switch_settings_checkbox('orders') \
            .switch_settings_checkbox('favorites') \
            .switch_settings_checkbox('information')
        main_page.open_page_via_side_menu('main_home_button')

        main_page.should_section_be_missing('orders') \
            .should_section_be_missing('favorites') \
            .should_section_be_missing('info')
