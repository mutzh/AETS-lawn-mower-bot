
# prompt = "Something went wrong. Please make sure to use the following format:\n" \
#                                  "'adress_1@host.com,adress_2@host.com,...,adress_n@host.com'\n" \
#                                  "Note that there are no Spaces between the adresses \n" \
#                                  "The Quotes are also essential"
# print( prompt)
from authorized import jason_write
from authorized import jason_read

adr = "mutzhdom@gmail.com,  aetsproject2020@gmail.com"
adr = adr.split(",")
print(adr)

if isinstance(adr, list):
  print("your object is a list !")
else:
    print("failure")
print(jason_write('authorized_adresses.json', adr))
jason_read('authorized_adresses.json')