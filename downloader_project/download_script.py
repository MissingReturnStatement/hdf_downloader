# -*- coding: utf-8 -*-
import requests
import os
import pandas as pd
import hashlib


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()

    try:
        with open(file_path, "rb") as f:
            data = f.read()  # Чтение всего файла в память
            hash_md5.update(data)

    except FileNotFoundError:
        return None

    return hash_md5.hexdigest()


def verify_md5(file_path, expected_md5):
    calculated_md5 = calculate_md5(file_path)

    if calculated_md5 is None:
        return False

    if calculated_md5.lower() == expected_md5.lower():
        return True
    else:
        return False
df = pd.read_csv('unique_files.csv')

token = 'eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImRlbnJvbTEzIiwiZXhwIjoxNzMwOTc2MTk5LCJpYXQiOjE3MjU3OTIxOTksImlzcyI6Imh0dHBzOi8vdXJzLmVhcnRoZGF0YS5uYXNhLmdvdiJ9.XWp8Y4vFC5S5OndD049AeV35ewp5OEfUHNXPp3r7_gZMQbJ1xcFHF5sQL3edxC6r5RGCjDlBAvS5qOOjGgbcPRKqxF6Ua-996PEKzX5f4JD2DxmhQdsm-5PPlvtRO_salQ3bdi90co5WYv3a-cA-YDTC1ek4Wk8o5NZbOSZP5TLbG_jRFrTfCsZNILaEEEUyPSkf4CnPohcgH3FHo1NooTTHwMoYBxXoSYQ8RIkyQBjfPyG-FzCDJ3jVKy3q1IYiWy_KPZDZXhFANr6BsHjiTaRUdnNv_zBtbKngcjimwHIeLmBv595Jwgmzu8nKW4sMxtJkZpGZAbMAHRtPeUsPdg'
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Authorization": f"Bearer {token}",
}
result_df = pd.DataFrame(['result','status_code','download_link','name','md5'])
for row in df.itertuples(index=False, name='Row'):
    response = requests.get(row.download_link, headers=headers, stream=True)
    output_file_path = os.path.join(os.getcwd(), row.name)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        try:
            with open(output_file_path, 'wb') as f:
                f.write(response.content)
            result_df = pd.concat([
                result_df,
                pd.DataFrame({
                    'result': [True],
                    'status_code': [response.status_code],
                    'download_link': [row.download_link],
                    'name': [row.name],
                    'md5': [verify_md5(output_file_path, row.md5sum)]
                })
            ], ignore_index=True)
        except Exception as e:
            result_df = pd.concat([
                result_df,
                pd.DataFrame({
                    'result': ['not ok'],
                    'status_code': [response.status_code],
                    'download_link': [row.download_link],
                    'name': [row.name],
                    'md5': [False]
                })
            ], ignore_index=True)
    else:
        result_df = pd.concat([
            result_df,
            pd.DataFrame({
                'result': ['not ok'],
                'status_code': [response.status_code],
                'download_link': [row.download_link],
                'name': [row.name],
                'md5': [False]
            })
        ], ignore_index=True)
result_df.to_csv('downloading_results.csv',index=False)