import requests

API_BASE_URL = 'https://demowebshop.tricentis.com'

catalog_product_ids = []
details_product_ids = []

start_product_id = 1
end_product_id = 100

for product_id in range(start_product_id, end_product_id):
    url = f'{API_BASE_URL}/addproducttocart/catalog/{product_id}/1/1'
    response = requests.post(url)
    response_json = response.json()
    if 'redirect' in response_json:
        details_product_ids.append(product_id)
    elif 'No product found with the specified ID' in response_json['message']:
        break
    else:
        catalog_product_ids.append(product_id)
