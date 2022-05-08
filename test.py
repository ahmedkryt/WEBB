import csv

with open('static/csv/person.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';', quotechar='"')
    for i in reader:
        print(i['email'])
        print(i['password'])
