# this file takes a python list of email adresses and checks if they exist in the real world by pinging the smtp server

def validate_adresses(adress_list):
    from validate_email import validate_email
    import dns

    # all_valid = True
    for adress in adress_list:
        # validation_status = all_valid and validate_email(adress, verify=True)

        verify = validate_email(email_address=adress, check_regex=True, from_address='aetsproject2020@gmail.com', debug=True)
        print(bool(verify))
    # return validation_status


# test call
adr = ['mutzhdom@gmail.com', 'dominic.mutzhas@hm.edu', 'aetsproject2020@gmail.com', "falkdrexel@gmail.com"]
# adr = adr.split(",,")
print(adr)
print(len(adr))
a = validate_adresses(adr)

