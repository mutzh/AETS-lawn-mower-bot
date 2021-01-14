def jason_write(filename, list):
    import json

    with open(filename, 'w') as f:
        json.dump(list, f)


list = ["mutzhdom@gmail.com", "aetsproject2020@gmail.com"]
jason_write('authorized_adresses.json', list)

def jason_read(filename):
    import json

    with open(filename, 'r') as myfile:
        data = myfile.read()

        obj = json.loads(data)
        print(obj)


jason_read('authorized_adresses.json')