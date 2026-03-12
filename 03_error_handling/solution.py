# Напиши решение здесь
import os
import json
class FileHandler:
    def file_read(self):
        try:
            with open('data.txt') as data_file:
                data = data_file.read()
            with open('log.txt', 'w') as log_file:
                log_file.write(data)
        except FileNotFoundError:
            with open('log.txt', 'w') as log_file:
                log_file.write('ERROR')
handler = FileHandler()
handler.file_read()
