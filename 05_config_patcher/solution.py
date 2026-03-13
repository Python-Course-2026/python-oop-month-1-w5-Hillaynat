# Напиши решение здесь
import os
import json
def replace_bool(file_name):
    if not os.path.exists(file_name):
        print(f"Ошибка: файл {file_name} не найден")
        return
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    new_text = text.replace('DEBUG=False', 'DEBUG=True')
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(new_text)
    print(f"Файл {file_name} успешно обновлен: DEBUG=False -> DEBUG=True")
replace_bool('config.env')