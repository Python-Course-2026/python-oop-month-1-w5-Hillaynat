import csv
import json
csv_file= 'users.csv'
json_file= 'users.json'
def convert(filename):
    data = []
    with open(filename) as csvfile :
        reader = csv.DictReader(filename)
        for row in reader:
            data.append(row)
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile)
convert('users.csv')

