
# prompt = "Something went wrong. Please make sure to use the following format:\n" \
#                                  "'adress_1@host.com,adress_2@host.com,...,adress_n@host.com'\n" \
#                                  "Note that there are no Spaces between the adresses \n" \
#                                  "The Quotes are also essential"
# print( prompt)
# from authorized import jason_write
# from authorized import jason_read

# adr = "mutzhdom@gmail.com,aetsproject2020@gmail.com"



# str = "aetsproject202\r\n0@gmail.com\r\n"
#
# print(str.translate({ord(i): None for i in '\r\n'}))

import delete_mail

import imaplib


# email_user = 'aetsproject2020@gmail.com'
# password = 'Info4Ever'
# imap_url = 'imap.gmail.com'



# import subprocess
# subprocess.call("./Shutdown.sh")
address_string = "photo, photo, photo///sadfasgfdfagarg"

cut_list = address_string.split("///")
address_string = str(cut_list)

address_string = address_string.translate({ord(i): None for i in ']'})
address_string = address_string.translate({ord(i): None for i in '['})
address_string = address_string.translate({ord(i): None for i in "'"})

address_list = address_string.split(",")
print(address_list)




