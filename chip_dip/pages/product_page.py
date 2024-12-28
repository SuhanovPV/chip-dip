import allure
from selene import browser
from selenium.webdriver import ActionChains, Keys


class ProductPage:
    @staticmethod
    def _open(product_name: str):
        with allure.step(f'Open product {product_name} page'):
            browser.open(f'/product/{product_name.lower()}')

    @staticmethod
    def _set_quantity(quantity):
        with allure.step('Set quantity for product'):
            browser.element('#ordering .input_qty').click()
            ActionChains(browser.driver).send_keys(Keys.DELETE).perform()
            browser.element('#ordering .input_qty').type(quantity)

    @staticmethod
    def _add_to_cart():
        with allure.step('Click button add to cart'):
            browser.element('[data-id="ordering"]').click()

    def add_product_to_cart(self, product: str, quantity: int = 1):
        with allure.step(f'Add f{product} to cart with quantity {quantity}'):
            self._open(product)
            if quantity > 1:
                self._set_quantity(quantity)
            self._add_to_cart()

    def add_products_to_cart(self, products: dict):
        with allure.step(f'Add products {list(products.keys())} to cart'):
            for product, quantity in products.items():
                self.add_product_to_cart(product, quantity)
