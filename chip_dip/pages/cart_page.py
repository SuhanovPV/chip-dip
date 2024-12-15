from selene import browser, have


class CartPage:
    @staticmethod
    def open():
        browser.open('/cart')

    @staticmethod
    def should_present_products(products: dict):
        browser.all('.cart__item .name').should(have.texts(*[x for x in products.keys()]))

    @staticmethod
    def clear():
        browser.element('#delete_checked').click()
        browser.element('#fancyConfirm_ok').click()

    @staticmethod
    def check_cart_empty():
        browser.element('#cart_empty h3').should(have.exact_text('Сейчас в корзине нет товаров'))

    @staticmethod
    def order_goods():
        browser.element('#cart_form [type="submit"]').click()
