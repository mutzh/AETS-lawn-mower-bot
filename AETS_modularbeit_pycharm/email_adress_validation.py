# this file takes a python list of email adresses and checks if they exist in the real world by pinging the smtp server

def validate(adress_list):
    from validate_email import validate_email

    all_valid = True
    for adress in adress_list:
        all_valid = all_valid and validate_email(adress, verify=True)
    return all_valid


print(validate(["mutzhdom@gmail.com", "aetsproject2020@gmail.com"]))
