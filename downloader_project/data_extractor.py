import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame


class CustomDate:
    def __init__(self,dates_list = None, hours_list = None):
        self.dates_list = dates_list if dates_list is not None else []
        self.hours_list = hours_list if hours_list is not None else []

    def add_to_dates(self, item):
        self.dates_list.append(item)

    def add_to_hours(self,item):
        self.hours_list.append(item)

    def get_dates_list(self):
        return self.dates_list

    def get_hours_list(self):
        return self.hours_list

    def get_dates_list_item(self,item):
        if 0 <= item < len(self.dates_list):
            return self.dates_list[item]
        else:
            raise IndexError("Индекс находится вне диапазона списка dates_list")

    def get_hours_list_item(self,item):
        if 0 <= item < len(self.hours_list):
            return self.hours_list[item]
        else:
            raise IndexError("Индекс находится вне диапазона списка hours_list")


def get_customdate_object(csv_file: DataFrame) -> CustomDate:
    df = pd.read_csv(csv_file)
    date_list = df['date'].to_list()
    custom_date_obj = CustomDate()
    for i in range(len(date_list)):
        custom_date_obj.add_to_dates(date_list[i].split()[0])
        custom_date_obj.add_to_hours(date_list[i].split()[1][:8])
    return custom_date_obj

custom_date_object = get_customdate_object('target.csv')
#print(custom_get_object.get_dates_list())
#print(custom_get_object.get_hours_list())


df = pd.read_csv('target.csv')
date_list = df['date'].to_list()
#print(date_list)