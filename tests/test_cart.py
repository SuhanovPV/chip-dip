import pytest
from chip_dip.data.Order import order_delivery
from chip_dip.pages.cart_page import CartPage
from chip_dip.pages.order_page import OrderPage
from chip_dip.pages.product_page import ProductPage


@pytest.mark.usefixtures("login")
class TestCart:
    def test_add_good_to_cart(self):
        product_page = ProductPage()
        products = {'ADM660ARZ-REEL7': 5, 'ICL7660CPAZ': 2}
        product_page.add_products_to_cart(products)

        cart = CartPage()
        cart.open()
        cart.should_present_products(products)
        # Teardown
        cart.clear()

    def test_clear_cart(self):
        product_page = ProductPage()
        products = {'ADM660ARZ-REEL7': 5, 'ICL7660CPAZ': 2}
        product_page.add_products_to_cart(products)

        cart = CartPage()
        cart.open()
        cart.should_present_products(products)
        cart.clear()

    def test_get_order(self):
        product_page = ProductPage()
        products = {'ADM660ARZ-REEL7': 5, 'ICL7660CPAZ': 2}
        product_page.add_products_to_cart(products)

        cart = CartPage()
        cart.open()
        cart.order_goods()
        order_page = OrderPage()
        order_page.fill_oder_form(order_delivery)
        order_page.should_set_order_address(order_delivery)

        cart.open()
        cart.clear()
