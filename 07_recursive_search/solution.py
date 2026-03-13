# Напиши решение здесь
import os
import json
def find_txt(folder, output_file):
    txt_list = []
    if not os.path.exists(folder):
        print(f"Ошибка: папка {folder} не найдена")
        return
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                full_path = os.path.join(root, file)
                txt_list.append(full_path)
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_path in txt_list:
            f.write(f"{file_path}\n")
    print(f"Найдено {len(txt_list)} .txt файлов. Результат сохранен в {output_file}")
find_txt('project', 'found.txt')