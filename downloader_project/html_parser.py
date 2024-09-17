import requests
import re
from data_extractor import custom_date_object
from bs4 import BeautifulSoup

URL = 'https://ladsweb.modaps.eosdis.nasa.gov/search/order/4/MYD021KM--61,MOD021KM--61/date/DB/84.8,56.7,85.1,56.4'
TEST_URL = 'https://ladsweb.modaps.eosdis.nasa.gov/search/order/4/MYD021KM--61,MOD021KM--61/2021-10-17..2021-10-17/DB/84.8,56.7,85.1,56.4'
JSON_URL = 'https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/details?products=MOD021KM&temporalRanges=2021-10-17..2021-10-17&regions=[BBOX]W84.8 N56.7 E85.1 S56.4 '

response = requests.get(JSON_URL)
data = response.json()
print(data)

from urllib import request


local_filename = 'downloaded_file'
def download_progress_hook(count, block_size, total_size):
    """
    Функция обратного вызова, используемая для отслеживания прогресса скачивания.
    :param count: Количество загруженных блоков
    :param block_size: Размер блока в байтах
    :param total_size: Общий размер файла
    """
    total_downloaded = count * block_size
    percent = (total_downloaded / total_size) * 100
    print(f"\rСкачано {total_downloaded} из {total_size} байт ({percent:.2f}%)", end='')
def download_file(url, filename):
    # Загружаем файл и сохраняем его по указанному пути, передавая функцию обратного вызова
    request.urlretrieve(url, filename, reporthook=download_progress_hook)

#@download_file('https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/MOD021KM.A2021290.1555.061.2021291013411.hdf', local_filename)
# response = requests.get(TEST_URL)
# if response.status_code == 200:
#     html_content = response.text
#     print(html_content)
# else:
#     print(f'Ошибка: {response.status_code}')