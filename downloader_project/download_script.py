import requests
import os

# URL для скачивания HDF файла
url = 'https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/MOD021KM.A2024064.1630.061.2024065024954.hdf'  # Замените на реальный URL
token = 'eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImRlbnJvbTEzIiwiZXhwIjoxNzMwOTc2MTk5LCJpYXQiOjE3MjU3OTIxOTksImlzcyI6Imh0dHBzOi8vdXJzLmVhcnRoZGF0YS5uYXNhLmdvdiJ9.XWp8Y4vFC5S5OndD049AeV35ewp5OEfUHNXPp3r7_gZMQbJ1xcFHF5sQL3edxC6r5RGCjDlBAvS5qOOjGgbcPRKqxF6Ua-996PEKzX5f4JD2DxmhQdsm-5PPlvtRO_salQ3bdi90co5WYv3a-cA-YDTC1ek4Wk8o5NZbOSZP5TLbG_jRFrTfCsZNILaEEEUyPSkf4CnPohcgH3FHo1NooTTHwMoYBxXoSYQ8RIkyQBjfPyG-FzCDJ3jVKy3q1IYiWy_KPZDZXhFANr6BsHjiTaRUdnNv_zBtbKngcjimwHIeLmBv595Jwgmzu8nKW4sMxtJkZpGZAbMAHRtPeUsPdg'
# Путь к директории, куда будет сохранен файл
output_dir = 'C:\\Users\\mrdea\\PycharmProjects'

# Имя файла, который вы хотите сохранить
file_name = 'MOD021KM.A2024064.1630.061.2024065024954.hdf'  # Убедитесь, что используете правильное имя файла

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Authorization": f"Bearer {token}",
}

# Используем метод get или post в зависимости от вашего запроса
response = requests.get(url, headers=headers, stream=True)
# Полный путь к файлу
output_file_path = os.path.join(output_dir, file_name)

# Отправка GET-запроса на скачивание файла
#response = requests.get(url)

# Проверка на успешный запрос
if response.status_code == 200:
    # Создание директории, если она не существует
    os.makedirs(output_dir, exist_ok=True)

    # Запись содержимого в файл
    with open(output_file_path, 'wb') as f:
        f.write(response.content)

    print(f"Файл успешно скачан и сохранен по пути: {output_file_path}")
else:
    print(f"Ошибка при скачивании файла: {response.status_code}")