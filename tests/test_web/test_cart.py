import pytest
import allure

from chip_dip.data.Order import order_delivery
from chip_dip.pages.cart_page import CartPage
from chip_dip.pages.order_page import OrderPage
from chip_dip.pages.product_page import ProductPage

@allure.suite('Website')
@allure.parent_suite('Chip Dip services')
@allure.sub_suite('Cart tests')
@allure.epic('Cart')
@allure.story('Tests work with cart')
@pytest.mark.usefixtures("browser_settings")
class TestCart:

    @allure.tag('web', 'cart')
    @allure.title('Add product to cart')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_good_to_cart(self, clear_cart):
        product_page = ProductPage()
        products = {'ADM660ARZ-REEL7': 5, 'ICL7660CPAZ': 2}
        product_page.add_products_to_cart(products)

        cart = CartPage()
        cart.open()
        cart.should_present_products(products)

    @allure.tag('web', 'cart')
    @allure.title('Add remove all product from cart')
    @allure.severity(allure.severity_level.MINOR)
    def test_clear_cart(self, clear_cart):
        product_page = ProductPage()
        products = {'ADM660ARZ-REEL7': 5, 'ICL7660CPAZ': 2}
        product_page.add_products_to_cart(products)

        cart = CartPage()
        cart.open()
        cart.should_present_products(products)
        cart.clear()
        cart.should_be_empty()

    @allure.tag('web', 'cart')
    @allure.title('Ordering product')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_order(self, clear_cart):
        product_page = ProductPage()
        products = {'ADM660ARZ-REEL7': 5, 'ICL7660CPAZ': 2}
        product_page.add_products_to_cart(products)

        cart = CartPage()
        cart.open()
        cart.order_goods()
        order_page = OrderPage()
        order_page.fill_oder_form(order_delivery)
        order_page.should_set_order_address(order_delivery)
