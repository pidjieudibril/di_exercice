import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'name': 'iphone 9',
            'price': 799,
            'remains': True
        },

        {
            'name': 'Macbook Pro',
            'price': 4799,
            'remains': False
        },

        {
            'name': 'Apple Watch',
            'price': 10799,
            'remains': True
        },

        {
            'name': 'Apple stand pro',
            'price': 99999,
            'remains': True
        },
    ]
    with open(dst_file, 'w') as file_obj:
        json.dump(data, file_obj)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj)
    return data
