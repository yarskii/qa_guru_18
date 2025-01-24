import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def open_cart():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver_options.add_argument('--disable-gpu')
    driver_options.add_argument('--no-sandbox')
    browser.config.driver_options = driver_options

    browser.config.base_url = 'https://demowebshop.tricentis.com/cart'
