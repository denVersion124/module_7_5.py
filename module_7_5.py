import os
import time
directory = os.getcwd()

for root, dirs, files in os.walk(directory): # Проходим по всем каталогам и файлам в указанной директории
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)  # Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматируем время
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)


print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')