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

# lst = jason_read('authorized_adresses.json')
# str1 = " "
# conv_str = (str1.join(lst))
# conv_str = conv_str[0:-2]
# print (conv_str)



