import pandas as pd
from pandas import read_csv

df = read_csv('nasa_files.csv')
df.to_excel('nasa_files.xlsx',index=False, engine='openpyxl')
