import requests
import re

URL = 'https://ladsweb.modaps.eosdis.nasa.gov/search/order/4/MYD021KM--61,MOD021KM--61/date/DB/84.8,56.7,85.1,56.4'
TEST_URL = 'https://ladsweb.modaps.eosdis.nasa.gov/search/order/4/MYD021KM--61,MOD021KM--61/2021-10-17..2021-10-17/DB/84.8,56.7,85.1,56.4'

response = requests.get(TEST_URL)
if response.status_code == 200:
    html_content = response.text
    print(html_content)
else:
    print(f'Ошибка: {response.status_code}')