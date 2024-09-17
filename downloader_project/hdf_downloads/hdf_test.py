import h5py

# Открываем HDF файл
with h5py.File('MOD021KM.A2024064.1630.061.2024065024954.hdf', 'r') as hdf_file:
    # Просматриваем содержимое файла
    print("Содержимое файла :")
    print(list(hdf_file.keys()))  # Показывает основные группы в файле