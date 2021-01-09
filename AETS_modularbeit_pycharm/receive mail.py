import easyimap as e
from subprocess import *

# wir brauchen noch etwas mit dem wir den event "email ist eingegangen" bemerken und unsere python scripts triggern


#man könnte es so machen, dass:
#1)das programm immer die neueste mail anschaut, solange bis:
#2.a) entweder keine ungelesenen Mails mehr da sind
#2.b) eine neue autorisierte mail geöffnet wurde--> abschicken eines fotos. dann wieder zurück zu 1)






#MAIL IM SPAMFOLDER
# wir könnten versuchen nur ein Postfach zu haben dann hat sich das problem

#setup email and password for the account that is supposed to be read
email_user = 'aetsproject2020@gmail.com'
password = 'Info4Ever'

#connect to the gmail server
server = e.connect('imap.gmail.com', email_user, password, 'Inbox', 587)




#get list of unseen emails
unseen_emails = server.unseen(10)


#iterate through the list
for unseen_email in unseen_emails:
    if unseen_email.from_addr == 'aetsproject2020@gmail.com':

        print(unseen_email.body)
#       define and call subprocess CHANGE THE CALL WITH "pyton" TO A CALL WITH "python3" for the raspberry
        subproc = Popen(['python', 'send_mail_prototype.py'])
        subproc.wait()
        print('mail sent')
        print('------------------')







