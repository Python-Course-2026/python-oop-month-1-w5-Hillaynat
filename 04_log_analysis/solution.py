# Напиши решение здесь
import os
import json
def log_reader(filename, output):
    count = 0
    with open(filename, 'r', encoding='utf-8') as log_file:
        for line in log_file:
            if '404' in line:
                count += 1
    with open(output, 'w', encoding='utf-8') as output_file:
        words = f'Найдено: {str(count)} с ошибкой 404'
        output_file.write(words)
print(log_reader('server.log', 'stats.txt'))