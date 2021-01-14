
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
print("the number of mails received is: ", len(unseen_emails))

# iterate through the list
for unseen_email in unseen_emails:
    print(unseen_email.body)

    # check if e-mail adress is authorized
    for recipient in authorized_email_recipients:
        print(recipient)
        if recipient in unseen_email.from_addr and unseen_email.body == "photo":
            # take picture and save it in current folder
            Webcam.take_picture(filename)

    # #       define and call subprocess CHANGE THE CALL WITH "pyton" TO A CALL WITH "python3" for the raspberry
    #         subproc = Popen(['python3', 'send_mail_attachment.py'])
    #         subproc.wait()

            send_mail.attachment(recipient, filename)
            print('mail sent to: ', recipient)
            print('------------------')
        elif recipient in unseen_email.from_addr and unseen_email.body == "list":
            send_mail.text(recipient, str(authorized_email_recipients))

# delete all mails from the account
time.sleep(10)
delete.all_mails(email_user, password, imap_url)






