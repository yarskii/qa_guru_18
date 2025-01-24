from selene import browser, have
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DemoShopUI:

    def open_cart(self, cookie):
        browser.open('/')
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
        browser.open('/')

    def checking_shopping_cart(self):
        if browser.all('.cart-item-row').should(have.size_greater_than_or_equal(1)):
            logging.info('Товар находится в корзине.')
