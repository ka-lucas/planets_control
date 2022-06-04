import json


def get_data():
    with open('bancodedados.json', 'r', encoding='utf8') as f:
        return json.load(f)


def insert_data(data):
    with open('bancodedados.json', 'w', encoding='utf8') as f:
        data = json.dumps(data, indent=4)
        f.write(data)
