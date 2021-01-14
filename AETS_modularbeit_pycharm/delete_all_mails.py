def delete_all_mails(user, password, imap_url):

   import imaplib

   box = imaplib.IMAP4_SSL(imap_url)
   box.login(user, password)
   box.select('INBOX')
   typ, data = box.search(None, 'ALL')
   print(data[0].split())
   for num in data[0].split():
      box.store(num, '+X-GM-LABELS', '\\Trash')
   box.expunge()
   box.close()
   box.logout()






