
import easyimap as e
from subprocess import *
import Webcam
import send_mail
import time
import delete
import authorized
import email_adress_validation

# ESTABLISH CONNECTION TO THE IMAP SERVER AND FETCH THE UNSEEN EMAILS
# setup variables for the following processes
email_user = 'aetsproject2020@gmail.com'
password = 'Info4Ever'
imap_url = 'imap.gmail.com'
authorized_email_recipients = authorized.jason_read('authorized_adresses.json')
root_email_user = "aetsproject2020@gmail.com"
print(type(authorized_email_recipients))
# define filename for the attachment
filename = "image.jpg"

# establish connection to the gmail server
con = e.connect(imap_url, email_user, password, 'Inbox', 587)

# get list of unseen emails
unseen_emails = con.unseen(10)
unseen_emails_number = len(unseen_emails)
print("the number of mails received is: ", unseen_emails_number)
# ----------------------------------------------------------------------------------------------------------------

# LOOP FOR PROCESSING AUTHORIZED E-MAILS:
# If there are 0 unseen emails, stop the script here, else proceed
if unseen_emails_number < 1:
    pass

else:
    # iterate through the list
    for unseen_email in unseen_emails:
        if "Reset" in unseen_email.body and "[" not in unseen_email.body:
            authorized.jason_write('authorized_adresses.json', root_email_user)

        # check if e-mail adress is authorized
        for authorized_recipient in authorized_email_recipients:
            print('authorized: ', authorized_recipient)
            print('sender: ', unseen_email.from_addr)

            # if condition to send a picture
            if authorized_recipient in unseen_email.from_addr and "Photo" in unseen_email.body and "[" not in unseen_email.body:
                # take picture and save it in current folder
                Webcam.take_picture(filename)

                send_mail.with_attachment(authorized_recipient, filename)
                print('mail sent to: ', authorized_recipient)
                print('------------------')

            # condition to view the list of authorized e-mails
            elif authorized_recipient in unseen_email.from_addr and "List" in unseen_email.body and "[" not in unseen_email.body:
                send_mail.text(authorized_recipient, str(authorized_email_recipients))

            # condition to edit the list of authorized e-mails
            elif authorized_recipient in unseen_email.from_addr and "[" in unseen_email.body:
                adress_list = unseen_email.body
                validation_status = email_adress_validation.validate(adress_list)
                # if all adresses are valid, update the list in the json file
                if validation_status is True:
                    send_mail.text(authorized_recipient, "All email adresses were validated and the list of authorized emails..."
                                                         "was updated sucessfully")
                    authorized.jason_write('authorized_adresses.json', unseen_email.body)
                else:  # send an error message
                    prompt = "There was a mistake. Either one of the e-mail adresses was not valid, or there was a problem with ..." \
                             "the input format. The body of the e-mail must only contain a list of valid e-mail adresses in ..." \
                             " the following format: '[adress_1, adress_2, ..., adress_n]'. Please pay attention to using ..." \
                             "the correct parenthesis when retrying. "
                    send_mail.text(send_mail.text(authorized_recipient, prompt))





    # delete all mails from the account
    time.sleep(10)
    delete.all_mails(email_user, password, imap_url)




    # #       define and call subprocess CHANGE THE CALL WITH "pyton" TO A CALL WITH "python3" for the raspberry
        #         subproc = Popen(['python3', 'send_mail_attachment.py'])
        #         subproc.wait()

