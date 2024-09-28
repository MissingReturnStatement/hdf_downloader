import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame


class CustomDate:
    def __init__(self,df = None,dates_list = None, hours_list = None):
        if df is not None:
            self.dates_list = df['date'].apply(lambda x: x.split()[0]).tolist()
            self.hours_list = df['date'].apply(lambda x: x.split()[1][:8]).tolist()
        else:
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

    def get_custom_object_from_csv(self, csv_file_name: str):
        df = pd.read_csv(csv_file_name)
        date_list = df['date'].to_list()
        for date in date_list:
            self.add_to_dates(date.split()[0])
            self.add_to_hours(date.split()[1][:8])
