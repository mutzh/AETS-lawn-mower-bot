# this script is the hearpice of the architecture.
# it helps to do different things when receiving an email from a list of authorized users:
# 1. it sends a picture
# 2. it sends a list of the authorized email users
# 3. it changes the list of authorized users
# furthermore it also includes the possibiliy to reset the list of authorized users to contain only a fixed root user

import easyimap as e
from subprocess import *
import Webcam
import send_mail
import time
import delete
import authorized

# ESTABLISH CONNECTION TO THE IMAP SERVER AND FETCH THE UNSEEN EMAILS
# setup variables for the following processes
email_user = 'aetsproject2020@gmail.com'
password = 'Info4Ever'
imap_url = 'imap.gmail.com'
authorized_email_recipients = authorized.jason_read('authorized_adresses.json')
root_email_user = "aetsproject2020@gmail.com"


# define filename for the attachment
filename = "image.jpg"

# establish connection to the gmail server
con = e.connect(imap_url, email_user, password, 'Inbox', 587)

# get list of unseen emails
unseen_emails = con.unseen(10)
unseen_emails_number = len(unseen_emails)
# print("the number of mails received is: ", unseen_emails_number)
# ----------------------------------------------------------------------------------------------------------------

# LOOP FOR PROCESSING AUTHORIZED E-MAILS:
# If there are 0 unseen emails, stop the script here, else proceed
if unseen_emails_number < 1:
    pass

else:
    # iterate through the list
    for unseen_email in unseen_emails:

        if "Reset" in unseen_email.body and "@" not in unseen_email.body:
            authorized.jason_write('authorized_adresses.json', root_email_user)
            prompt = "The list of authorized users has been reset to ONLY the root_email_user: " + str(root_email_user)
            send_mail.text(root_email_user, prompt, " Mower Reset Success")
        else:
            
            # check if e-mail adress is authorized
            for authorized_recipient in authorized_email_recipients:

                # if condition to send a picture
                if authorized_recipient in unseen_email.from_addr and "Photo" in unseen_email.body and "@" not in unseen_email.body:
                    Webcam.take_picture(filename)
                    send_mail.with_attachment(authorized_recipient, filename)

                # condition to view the list of authorized e-mails
                elif authorized_recipient in unseen_email.from_addr and "List" in unseen_email.body and "@" not in unseen_email.body:

                    prompt = "Here is the list of authorized users: \n" + str(authorized_email_recipients) + "\n If you wish to change the list, please note: \n\n" \
                                 "Here is an example for the Input format:\n" \
                                 '''"adress_1@host.com, adress_2@host.com,..., adress_n@host.com"\n''' \
                                 "It is essential to : \n" \
                                 "1. have quotation marks around the list\n" \
                                 "2. separate them ONLY with ONE comma and ONE space, like shown in the example above"
                    send_mail.text(authorized_recipient, prompt, "Mower Authorized Users")

                # Update Authorized List
                elif authorized_recipient in unseen_email.from_addr and "@" in unseen_email.body:

                    adress_string = unseen_email.body
                    adress_string = adress_string.translate({ord(i): None for i in '\r\n'})
                    adress_list = adress_string.split(", ")
                    authorized.jason_write('authorized_adresses.json', adress_list)

                    new_list = authorized.jason_read('authorized_adresses.json')
                    prompt = "All email adresses were validated and the list of authorized emails was updated sucessfully" \
                              "The new list is: \n " + str(new_list)

                    send_mail.text(authorized_recipient, prompt, "Mower Changed Authorization Success")








    # delete all mails from the account
    time.sleep(5)
    delete.all_mails(email_user, password, imap_url)




    # #       define and call subprocess CHANGE THE CALL WITH "pyton" TO A CALL WITH "python3" for the raspberry
        #         subproc = Popen(['python3', 'send_mail_attachment.py'])
        #         subproc.wait()

