import requests
import logging

from config import API_BASE_URL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DemoShopAPI:

    def add_product_to_cart_details(self, product_id, quantity):
        url = f'{API_BASE_URL}/addproducttocart/details/{product_id}/1'
        data = {f'giftcard_{product_id}.RecipientName': 'Bob Bob',
                f'giftcard_{product_id}.RecipientEmail': 'qwerty@qwerty.com',
                f'giftcard_{product_id}.SenderName': 'Ros Ros',
                f'giftcard_{product_id}.SenderEmail': 'asdfgh@qwerty.com',
                f'product_attribute_{product_id}_7_1': 1,
                f'addtocart_{product_id}.EnteredQuantity': f'{quantity}'}
        response = requests.post(url, data=data)

        return response

    def add_product_to_cart_catalog(self, product_id, quantity):
        url = f'{API_BASE_URL}/addproducttocart/catalog/{product_id}/1/{quantity}'
        response = requests.post(url)

        return response

    def receive_a_response_to_the_request(self, response):
        response_json = response.json()
        try:
            if response_json['success']:
                logging.info('Товар успешно добавлен.')
            elif not response_json['success']:
                logging.error(f'Ошибка при добавлении товара: {response_json['message']}')
        except KeyError:
            logging.error(f'Ошибка при добавлении товара: {response_json}')
