import allure
import pytest
from allure_commons.types import AttachmentType

from models.demo_shop_api import DemoShopAPI
from models.demo_shop_ui import DemoShopUI
from config import catalog_product_ids, details_product_ids

QUANTITY = 1

product = DemoShopAPI()
cart = DemoShopUI()


@allure.feature('Добавление товара в корзину')
@allure.story('Добавление продукта через API и проверка в UI')
@pytest.mark.parametrize("product_id", catalog_product_ids)
def test_add_to_cart_from_catalog(product_id):
    with allure.step("Отправка запроса для добавления товара в корзину"):
        response = product.add_product_to_cart_catalog(product_id, QUANTITY)

        assert response.status_code == 200, "Не удалось добавить продукт"

        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with allure.step("Получаем JSON-ответ"):
        product.receive_a_response_to_the_request(response)

    with allure.step("Получаем куки добавления товара в корзину"):
        cookie = response.cookies.get('Nop.customer')

    with allure.step("Открытие страницы корзины и добавление куки"):
        cart.open_cart(cookie)

    with allure.step("Проверка наличия товара в корзине"):
        cart.checking_shopping_cart()


@allure.feature('Добавление товара в корзину')
@allure.story('Добавление продукта через API и проверка в UI')
@pytest.mark.parametrize('product_id', details_product_ids)
def test_add_to_cart_from_details(product_id):
    with allure.step("Отправка запроса для добавления товара в корзину"):
        response = product.add_product_to_cart_details(product_id, QUANTITY)

        assert response.status_code == 200, "Не удалось добавить продукт"

        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with allure.step("Получаем JSON-ответ"):
        product.receive_a_response_to_the_request(response)

    with allure.step("Получаем куки добавления товара в корзину"):
        cookie = response.cookies.get('Nop.customer')

    with allure.step("Открытие страницы корзины и добавление куки"):
        cart.open_cart(cookie)

    with allure.step("Проверка наличия товара в корзине"):
        cart.checking_shopping_cart()
