#!/usr/bin/env python

# script supports either python2 or python3. You might need to change the above
# line to "python3" depending on your installation.
#
# Attempts to do HTTP Gets with urllib2(py2) urllib.requets(py3) or subprocess
# if tlsv1.1+ isn't supported by the python ssl module
#
# Will download csv or json depending on which python module is available
#

from __future__ import (division, print_function, absolute_import, unicode_literals)

import argparse
import os
import os.path
import shutil
import sys
import ssl
import time



def create_dir() -> str:
    folder_name = 'hdf_downloads'
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(f'Папка "{folder_name}" уже существует.')
    full_path = os.path.abspath(folder_name)
    return full_path


import requests

# Замените YOUR_TOKEN_HERE и PATH_TO_FILE на ваши значения
token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImRlbnJvbTEzIiwiZXhwIjoxNzMwOTc2MTk5LCJpYXQiOjE3MjU3OTIxOTksImlzcyI6Imh0dHBzOi8vdXJzLmVhcnRoZGF0YS5uYXNhLmdvdiJ9.XWp8Y4vFC5S5OndD049AeV35ewp5OEfUHNXPp3r7_gZMQbJ1xcFHF5sQL3edxC6r5RGCjDlBAvS5qOOjGgbcPRKqxF6Ua-996PEKzX5f4JD2DxmhQdsm-5PPlvtRO_salQ3bdi90co5WYv3a-cA-YDTC1ek4Wk8o5NZbOSZP5TLbG_jRFrTfCsZNILaEEEUyPSkf4CnPohcgH3FHo1NooTTHwMoYBxXoSYQ8RIkyQBjfPyG-FzCDJ3jVKy3q1IYiWy_KPZDZXhFANr6BsHjiTaRUdnNv_zBtbKngcjimwHIeLmBv595Jwgmzu8nKW4sMxtJkZpGZAbMAHRtPeUsPdg"
file_path = "PATH_TO_FILE"
#output_file_path = create_dir()
output_dir = '/home/mrdea/PycharmProjects/hdf_downloader/downloader_project/hdf_downloads'

#url = f"https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/{file_path}"
url = 'https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/MOD021KM.A2024064.1630.061.2024065024954.hdf'
file_name = 'MOD021KM.A2024064.1630.061.2024065024954.hdf'
output_file_path = os.path.join(output_dir, file_name)
# Заголовки запроса
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Authorization": f"Bearer {token}",
}

# Используем метод get или post в зависимости от вашего запроса
response = requests.get(url, headers=headers, stream=True)

if response.status_code == 200:
    # Запись содержимого в файл
    with open(output_file_path, 'wb') as f:
        f.write(response.content)
else:
    print(f"Ошибка: {response.status_code} - {response.text}")


