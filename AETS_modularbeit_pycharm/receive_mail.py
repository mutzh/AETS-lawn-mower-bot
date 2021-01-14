
import easyimap as e
from subprocess import *
import Webcam
import send_mail
import time
import delete

# setup email and password for the account that is supposed to be read
email_user = 'aetsproject2020@gmail.com'
password = 'Info4Ever'
imap_url = 'imap.gmail.com'
authorized_email_recipients = ['mutzhdom@gmail.com', 'aetsproject2020@gmail.com']

# define filename for the attachment
filename = "image.jpg"


# establish connection to the gmail server
con = e.connect(imap_url, email_user, password, 'Inbox', 587)

# get list of unseen emails
unseen_emails = con.unseen(10)
unseen_emails_number = len(unseen_emails)
print("the number of mails received is: ", unseen_emails_number)

# If there are 0 unseen emails, stop the script here, else proceed
if unseen_emails_number < 1:
    pass

else:
    # iterate through the list
    for unseen_email in unseen_emails:

        # check if e-mail adress is authorized
        for authorized_recipient in authorized_email_recipients:
            print('authorized: ', authorized_recipient)
            print('sender: ', unseen_email.from_addr)
            if authorized_recipient in unseen_email.from_addr and "Photo" in unseen_email.body :
                # take picture and save it in current folder
                Webcam.take_picture(filename)

        # #       define and call subprocess CHANGE THE CALL WITH "pyton" TO A CALL WITH "python3" for the raspberry
        #         subproc = Popen(['python3', 'send_mail_attachment.py'])
        #         subproc.wait()

                send_mail.attachment(authorized_recipient, filename)
                print('mail sent to: ', authorized_recipient)
                print('------------------')
            elif authorized_recipient in unseen_email.from_addr and "List" in unseen_email.body:
                send_mail.text(authorized_recipient, str(authorized_email_recipients))
            else:
                send_mail.text(authorized_recipient, "Sie haben eine ungültige Anfrage getätigt, bitte berücksichtigen..."
                                                     "Sie Gross- und Kleinschreibung versuchen es erneut. ..."
                                                     "Der erste Buchstabe sollte gross geschrieben sein.")

    # delete all mails from the account
    time.sleep(10)
    delete.all_mails(email_user, password, imap_url)






