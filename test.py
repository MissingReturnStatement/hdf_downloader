import pandas as pd

df = pd.read_excel('/home/mrdea/PycharmProjects/hdf_downloader/downloader_project/nasa_files.xlsx')
print(df[df['download_link'].unique()])
url = 'https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/MOD021KM.A2024064.1630.061.2024065024954.hdf'
url_ = 'https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/'
print(len(url))
print(len(url_))
print(url[63:])
