
import easyimap as e
from subprocess import *
import imaplib
import Webcam
import send_mail
import time
import delete

# wir brauchen noch etwas mit dem wir den event "email ist eingegangen" bemerken und unsere python scripts triggern


#man könnte es so machen, dass:
#1)das programm immer die neueste mail anschaut, solange bis:
#2.a) entweder keine ungelesenen Mails mehr da sind
#2.b) eine neue autorisierte mail geöffnet wurde--> abschicken eines fotos. dann wieder zurück zu 1)

#setup email and password for the account that is supposed to be read
email_user = 'aetsproject2020@gmail.com'
password = 'Info4Ever'
imap_url = 'imap.gmail.com'
authorized_email_recipients = ['aetsproject2020@gmail.com', 'mutzhdom@gmail.com']

#define filename for the attachment
filename = "image.jpg"


#establish connection to the gmail server
con = e.connect(imap_url, email_user, password, 'Inbox', 587)

#get list of unseen emails
unseen_emails = con.unseen(10)
print("the number of mails received is: ", len(unseen_emails))

#iterate through the list
for unseen_email in unseen_emails:
    print(unseen_email.body)
#hier soll das ding spater schauen ob dieser string in einem der strings aus
#der liste authorisierter emails ist
    #check if e-mail adress is authorized
    for recipient in authorized_email_recipients:
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

#delete all mails from the account
# time.sleep(10)
delete.all_mails(email_user, password, imap_url)






