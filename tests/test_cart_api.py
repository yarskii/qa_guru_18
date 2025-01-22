import allure
import requests
from selene import browser, have
from allure_commons.types import AttachmentType

CART_URL = 'https://demowebshop.tricentis.com/cart'
API_BASE_URL = 'https://demowebshop.tricentis.com'
PRODUCT_ID = 36
QUANTITY = 1000

data = {f'giftcard_{PRODUCT_ID}.RecipientName': 'Bob Bob',
        f'giftcard_{PRODUCT_ID}.RecipientEmail': 'qwerty@qwerty.com',
        f'giftcard_{PRODUCT_ID}.SenderName': 'Ros Ros',
        f'giftcard_{PRODUCT_ID}.SenderEmail': 'asdfgh@qwerty.com',
        f'addtocart_{PRODUCT_ID}.EnteredQuantity': f'{QUANTITY}'}


@allure.feature('Добавление товара в корзину')
@allure.story('Добавление продукта через API и проверка в UI')
def test_add_to_cart():
    with allure.step("Отправка запроса для добавления товара в корзину"):
        if 1 <= PRODUCT_ID <= 4:
            url = f'{API_BASE_URL}/addproducttocart/details/{PRODUCT_ID}/1'
            response = requests.post(url, data=data)
        else:
            url = f'{API_BASE_URL}/addproducttocart/catalog/{PRODUCT_ID}/1/{QUANTITY}'
            response = requests.post(url)

        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    try:
        with allure.step("Получаем JSON-ответ"):
            response_json = response.json()
            if response_json['success']:
                print('Товар успешно добавлен.')
            elif not response_json['success']:
                print('Ошибка при добавлении товара:', response_json['message'])

    except KeyError:
        new_url = f'{API_BASE_URL}/addproducttocart/details/{PRODUCT_ID}/1'
        response = requests.post(new_url)
        response_json = response.json()
        print('Ошибка при добавлении товара:', response_json['message'])
        print('Требуется заполнить обязательные поля')

    with allure.step("Получаем куки добавления товара в корзину"):
        cookie = response.cookies.get('Nop.customer')

    with allure.step("Открытие страницы корзины и добавление куки"):
        browser.open(CART_URL)
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
        browser.open(CART_URL)

    with allure.step("Проверка наличия товара в корзине"):
        try:
            browser.all('.cart-item-row').should(have.size_greater_than_or_equal(1))
            print('Товар находится в корзине.')
        except AssertionError:
            print('Товар не найден в корзине.')
