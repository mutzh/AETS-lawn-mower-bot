# sends mail from "aetsproject2020@gmail.com" to "recipient"
# both inputs have to be strings


def with_attachment(recipient, filename):

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    # define the attribute values for the email
    body = "I sent this mail by triggering the 'Receive mail' python script form my raspberry pi bitch!"
    subject = 'Mower Überwachung'

    # create multipart message object with suject body etc...
    msg = MIMEMultipart()
    msg['From'] = 'aetsproject2020@gmail.com'
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # create the attachment( in this library describe as a payload)  "part" for it to be attached to the message
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-strem')    # this opens a stream to send the attachment and closes it back up
    part.set_payload(attachment.read())    # get the attachment into the part
    encoders.encode_base64(part)    # encoding it with base_64 (just google its a standard encoding for emails)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    # attach this part to our message
    msg.attach(part)

    #   convert object to a string
    txt = msg.as_string()

    #   connect to the Gmail Server (here the SMTP Client) via port 587, and activating security tls protocol
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aetsproject2020@gmail.com', 'Info4Ever')

    # send mail and quit connection to server
    server.sendmail('aetsproject2020@gmail.com', recipient, txt)
    server.quit()


def text(recipient, text_body):

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # define the attribute values for the email
    body = text_body
    subject = 'List of Authorized users'

    #   create multipart message object with suject body etc...
    msg = MIMEMultipart()
    msg['From'] = 'aetsproject2020@gmail.com'
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    #   convert object to a string
    txt = msg.as_string()

    #   connect to the Gmail Server (here the SMTP Client) via port 587, and activating security tls protocol
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aetsproject2020@gmail.com', 'Info4Ever')

    # send mail and quit connection to server
    server.sendmail('aetsproject2020@gmail.com', recipient, txt)
    server.quit()



