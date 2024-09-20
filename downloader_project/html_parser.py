import requests
import pandas as pd
from tqdm import tqdm
from data_extractor import CustomDate
from pandas.core.interchange.dataframe_protocol import DataFrame
from datetime import datetime, timedelta, timezone


def parse_json(product: str, date: str) -> list[dict | int]:
    back_date = str(datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1))
    front_date = str(datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1))
    triplet_date = [back_date, date, front_date]
    triplet_json = []
    for item in triplet_date:
        standard_parse_url = f'https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/details?products={product}&temporalRanges={item}&regions=[BBOX]W84.8%20N56.7%C2%A0E85.1%C2%A0S56.4'
        response = requests.get(url=standard_parse_url)
        if response.status_code == 200:
            triplet_json.append(response.json())
        else:
            triplet_json.append(response.status_code)
    return triplet_json


def get_closest_time_row(product: str, date: str, time: str) -> dict:
    response_ = parse_json(product, date)
    min_time_range = timedelta.max
    closest_item = None
    closest_time_range = None
    check_list = []
    for obj in response_:
        if isinstance(obj, int):
            check_list.append({'status_code': obj})
        elif isinstance(obj, dict):
            for item in obj['content']:
                lidar_time = date + ' ' + time
                lidar_time = datetime.strptime(lidar_time, "%Y-%m-%d %H:%M:%S")
                target_time = datetime.strptime(item['start'], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
                lidar_time = lidar_time.replace(tzinfo=timezone(timedelta(hours=7)))
                time_range = abs(lidar_time - target_time)
                if time_range < min_time_range:
                    min_time_range = time_range
                    closest_item = item
                    closest_time_range = time_range
    return {'lidar_date': lidar_time.strftime("%Y-%m-%d %H:%M:%S"), 'name': closest_item['name'],
            'product': closest_item['products'],
            'illuminations': closest_item['illuminations'], 'start': closest_item['start'],
            'md5sum': closest_item['md5sum'],
            'download_link': closest_item['downloadsLink'], 'time_range': str(closest_time_range)}


def fill_table(df: DataFrame, custom_date_object: CustomDate, products: list[str]) -> DataFrame:
    i = 0
    with tqdm(total=len(custom_date_object.get_dates_list())) as pbar:
        i = 0
        for date, time in tqdm(zip(custom_date_object.get_dates_list(), custom_date_object.get_hours_list())):
            i+=1
            row_myd = get_closest_time_row(products[0], date, time)
            row_mod = get_closest_time_row(products[1], date, time)
            df = pd.concat([df, pd.DataFrame([row_myd])], ignore_index=True)
            df = pd.concat([df, pd.DataFrame([row_mod])], ignore_index=True)
            pbar.update(1)
            if i == 30:
                return df
        return df


#variables
csv_file_name = 'target.csv'
dates_df = pd.read_csv(csv_file_name)
custom_date = CustomDate(dates_df)
URL = 'https://ladsweb.modaps.eosdis.nasa.gov/search/order/4/MYD021KM--61,MOD021KM--61/date/DB/84.8,56.7,85.1,56.4'
TEST_URL = 'https://ladsweb.modaps.eosdis.nasa.gov/search/order/4/MYD021KM--61,MOD021KM--61/2021-10-17..2021-10-17/DB/84.8,56.7,85.1,56.4'
products = ['MYD021KM', 'MOD021KM']
columns = ['lidar_date', 'name', 'product', 'illuminations', 'start', 'md5sum', 'download_link', 'time_range']
files_table = pd.DataFrame(columns=columns)

files_table = fill_table(files_table, custom_date, products)
files_table.to_csv('nasa_files.csv', index=False)
#print(get_closest_time_row('MYD021KM',custom_date.get_dates_list()[455],custom_date.get_hours_list()[455]))
# print(json_['content'])
