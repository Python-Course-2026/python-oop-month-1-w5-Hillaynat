import csv
import json
def convert(users.csv,json_file):
    with open(users.csv) as users.csv:
        reader = csv.DictReader(users_csv)
        headers = users_csv.readline().split(',').strip()
        with open(users.json, 'w') as json_file:
            json.dump(reader, users, ensure_ascii=False)

