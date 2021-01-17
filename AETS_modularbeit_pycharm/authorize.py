def jason_write(filename, list):
    import json

    with open(filename, 'w') as f:
        json.dump(list, f)



def jason_read(filename):
    import json

    with open(filename, 'r') as myfile:
        data = myfile.read()

        obj = json.loads(data)

    return obj




