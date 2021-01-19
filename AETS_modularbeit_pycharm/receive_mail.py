#!/usr/bin/python3

# this script is the heartpice of the architecture.
# it helps to do different things when receiving an email from a list of authorized users:
    # 1. it sends a picture
    # 2. it sends a list of the authorized email users
    # 3. it changes the list of authorized users
# it also allows the following actions to be performed by a root email user ( that user is hardcoded in this script)
    # 1. Reset the list of authorized users to only the root user
    # 2. Shutdown the pi before pulling the cable


import easyimap as e
import subprocess
import Webcam
import send_mail
import time
import delete_mail
import authorize
import imaplib
from convert_word2list import word2list

# SETUP THE INITIAL VARIABLES FOR THIS SCRIPT
# connection parameters
email_user = 'aetsproject2020@gmail.com'
password = 'Info4Ever'
imap_url = 'imap.gmail.com'
# read the current list of authorized users from json file
authorized_email_recipients = authorize.jason_read('authorized_addresses.json')
# List of authorized emails can be reset to only root user
root_email_str = "herbert.palm@hm.edu"
# define filename for the attachment
filename = "image.jpg"

# WHILE LOOP THAT FUNCTIONS AS LISTENER
sleep_seconds = 3
deletion_iterator = 0
while True:
    # establish connection to the gmail server
    con = e.connect(imap_url, email_user, password, 'Inbox', 587)

    # get list of unseen emails
    unseen_emails = con.unseen(10)
    unseen_emails_number = len(unseen_emails)
    # print("the number of mails received is: ", unseen_emails_number)
    # ----------------------------------------------------------------------------------------------------------------

    # LOOP FOR PROCESSING AUTHORIZED E-MAILS:
    # If there are 0 unseen emails, stop the script here, else proceed
    # all responses are sent back to the respective e-mail address which performed the request
    if unseen_emails_number < 1:
        print("pass")
        pass

    else:
        # iterate through the list
        for unseen_email in unseen_emails:

            # Reset to root email address
            if root_email_str in unseen_email.from_addr and "Reset" in unseen_email.body:
                root_email_list = word2list(root_email_str)
                authorize.jason_write('authorized_addresses.json', root_email_list)
                authorized_email_recipients = authorize.jason_read('authorized_addresses.json')
                prompt = "The list of authorized addresses has was to ONLY the root_email_user: " + root_email_str
                send_mail.text(root_email_str, prompt, " Mower Reset Success")

            # shutdown raspi before cutting the power connection
            elif root_email_str in unseen_email.from_addr and "Shutdown" in unseen_email.body:
                # define and call subprocess CHANGE THE CALL WITH "python" TO A CALL WITH "python3" for the raspberry
                send_mail.text(root_email_str, "Shutdown in progress", "Raspberry Shutdown")
                time.sleep(10)
                subprocess.call("./Shutdown.sh")

            else:
                # check if e-mail address is authorized
                for authorized_recipient in authorized_email_recipients:
                    # check if the requesting address is authorized
                    if authorized_recipient not in unseen_email.from_addr:
                        pass

                    else:
                        # if condition to send a picture
                        if "Photo" in unseen_email.body:
                            Webcam.take_picture(filename)
                            send_mail.with_attachment(authorized_recipient, filename)

                        # View authorized e-mails
                        elif "List" in unseen_email.body:

                            prompt = "- Authorized addresses: \n  " + str(authorized_email_recipients) + "\n\n- When " \
                                     "changing the list, please use the format shown in the following example: \n" \
                                     "  address1@example.com, address2@example.com, address3@example.com/// \n\n" \
                                     "- It is essential to: \n" \
                                     "  1. Separate them with ONLY ONE comma, as shown in the example \n" \
                                     "  2. Abstain from Wrapping the addresses with quotation-marks or parenthesis\n" \
                                     "  3. Abstain from inserting the e-mail addresses in the form of links" \
                                     "  4. Include the tree backslashes appended to the last email."

                            send_mail.text(authorized_recipient, prompt, "Mower Authorized Users")

                        # Update Authorized List
                        elif "///" in unseen_email.body:

                            # update json which contains the list
                            address_string = unseen_email.body
                            # remove potential unwanted characters
                            address_string = address_string.translate({ord(i): None for i in '\r\n'})
                            address_string = address_string.translate({ord(i): None for i in '<'})
                            address_string = address_string.translate({ord(i): None for i in '>'})
                            address_string = address_string.translate({ord(i): None for i in ' '})
                            address_string = address_string.translate({ord(i): None for i in '''"'''})
                            # remove the rest of the email body(this turns the whole thing into a list)
                            cut_list = address_string.split("///", 1)[0]
                            # reconvert to string to split up into the respective email addresses
                            cut_string = str(cut_list)
                            # remove the characters that were added by splitting it up into a list
                            cut_string = cut_string.translate({ord(i): None for i in ']'})
                            cut_string = cut_string.translate({ord(i): None for i in '['})
                            cut_string = cut_string.translate({ord(i): None for i in "'"})
                            # split up into respective email addresses
                            address_list = cut_string.split(",")


                            authorize.jason_write('authorized_addresses.json', address_list)

                            # send a success mail with the new list to the requesting adress
                            new_list = authorize.jason_read('authorized_addresses.json')
                            prompt = "The list of authorized emails was updated successfully to: \n\n" + str(new_list)
                            send_mail.text(authorized_recipient, prompt, "Mower Changed Authorization Success")

                            # Update the variable with the authorized addresses for the whole while loop
                            authorized_email_recipients = authorize.jason_read('authorized_addresses.json')

        # delete all mails from the account, only every 20th iteration
        if deletion_iterator % 20 == 0:
            con = imaplib.IMAP4_SSL(imap_url)
            con.login(email_user, password)
            delete_mail.delete_days_before(con, 1)
        # delete.all_mails(email_user, password, imap_url)

    # let the script sleep, since it doesnt make sense to check every minute. maybe every 15 minutes is enough
    deletion_iterator += 1
    time.sleep(sleep_seconds)