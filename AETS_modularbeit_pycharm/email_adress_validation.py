# this file takes a python list of email adresses and checks if they exist in the real world by pinging the smtp server

def validate_adresses(adress_list):
    from validate_email import validate_email

    all_valid = True
    for adress in adress_list:
        validation_status = all_valid and validate_email(adress, verify=True)
    return validation_status


# test call
adr = "mutzhdom@gmail.com,aetsproject2020@gmail.com"
adr = adr.split(",")
print(adr)
a = validate_adresses(adr)
if a is True:
    print("yes")
