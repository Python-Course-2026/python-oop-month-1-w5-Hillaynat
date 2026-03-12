# Напиши решение здесь
import os
import json
def replace_bool(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

        new_line = text.replace('DEBUG=False', 'DEBUG=True')

    with open(file_name, 'w') as f:
        f.write(new_line)
replace_bool('config.env')