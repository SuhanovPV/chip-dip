from chip_dip.data.Order import Delivery

from selene import browser, have


class OrderPage:
    @staticmethod
    def select_delivery_type(delivery: Delivery):
        browser.element(f'//*[@id="howpickup_tabs"]//*[contains(text(),"{delivery.delivery_type}")]').click()

    @staticmethod
    def select_city(delivery: Delivery):
        browser.element('#select2-pvz_cities-container').click()
        browser.element(f'//ul[@class="select2-results__options"]//*[contains(text(), "{delivery.city}")]').click()

    @staticmethod
    def select_pick_up_point(delivery: Delivery):
        browser.element('#select2-pvz_ids-container').click()
        browser.element(
            f'//ul[@class="select2-results__options"]//*[contains(text(), "{delivery.street}, д {delivery.building}")]'
        ).click()

    @staticmethod
    def fill_comment(delivery: Delivery):
        browser.element('[name="clientdescription"]').type(delivery.comment)

    @staticmethod
    def should_set_order_address(delivery: Delivery):
        browser.element('#pvz_props .pvz-address').should(have.exact_text(
            f'{delivery.country}, г {delivery.city}, {delivery.street}, д {delivery.building}'
        ))

    def fill_oder_form(self, delivery: Delivery):
        self.select_delivery_type(delivery)
        self.select_city(delivery)
        self.select_pick_up_point(delivery)
        self.fill_comment(delivery)

