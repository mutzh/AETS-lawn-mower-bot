import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(email_receipient, )
email_user = 'aetsproject2020@gmail.com'
email_password = 'Info4Ever'
email_send = 'aetsproject2020@gmail.com'

subject = 'python mail'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='filename'
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
#the security that felix had in mind for us
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()