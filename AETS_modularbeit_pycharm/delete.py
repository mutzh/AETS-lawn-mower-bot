def all_mails(user, password, imap_url):

    import imaplib

    box = imaplib.IMAP4_SSL(imap_url)
    box.login(user, password)

    box.select('INBOX')
    typ, data = box.search(None, 'ALL')
    number_deleted_emails = len(data[0].split())

    for num in data[0].split():
        box.store(num, '+X-GM-LABELS', '\\Trash')
    box.expunge()
    box.close()
    box.logout()

    print("deleted emails: " + str(number_deleted_emails))
    print('All mails were moved to the Bin, where they will be automatically deleted after 30 days')




