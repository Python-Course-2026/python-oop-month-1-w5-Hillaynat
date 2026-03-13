# Напиши решение здесь
import os
import json
def check_file(filename_1, filename_2):
    if not os.path.exists(filename_1):
        print(f"Ошибка: файл {filename_1} не найден")
        return
    with open(filename_1, 'rb') as f1:
        data = f1.read(4)
    if data == b'\x89PNG':
        result = 'PNG'
    else:
        result = 'UNKNOWN'
    with open(filename_2, 'w', encoding='utf-8') as f2:
        f2.write(result)
    print(f"Результат: {result} (записан в {filename_2})")
check_file('file.bin', 'type.txt')
