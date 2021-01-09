import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import Webcam

#take picture and save it in current folder
Webcam.take_picture()


# def send_email(email_receipient, )

#define the attribute values for the email
photo_email_receipient = "f-drexel@gmx.de"
body = "I sent this mail by triggering the 'Receive mail' python script form my raspberry pi bitch!"
subject = 'Mower Überwachung'

#   create multipart message object with suject body etc...
msg = MIMEMultipart()
msg['From'] = 'aetsproject2020@gmail.com'
msg['To'] = photo_email_receipient
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

#create the attachment( in this library describe as a payload)  "part" for it to be attached to the message
filename = 'image.jpg'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-strem') # this opens a stream to send the attachment and closes it back up
part.set_payload(attachment.read()) # get the attachment into the part
encoders.encode_base64(part) # encoding it with base_64 (just google "basis" videos, its a standard encoding for emails)
part.add_header('Content-Disposition', "attachment; filename= "+filename)
#attach this part to our message
msg.attach(part)


#   convert object to a string
text = msg.as_string()

#   connect to the Gmail Server (here the SMTP Client) via port 587, and activating security tls protocol
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('aetsproject2020@gmail.com', 'Info4Ever')


#   send mail and quit connection to server
server.sendmail('aetsproject2020@gmail.com', photo_email_receipient, text)
server.quit()


#send attachment by triggering fs webcam
