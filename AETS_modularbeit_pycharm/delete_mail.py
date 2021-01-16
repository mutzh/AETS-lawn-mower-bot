def delete_days_before(con, folder, days_before):
    import datetime

    con.select('INBOX')
    before_date = (datetime.date.today() - datetime.timedelta(days_before)).strftime("%d-%b-%Y")  # date string, 04-Jan-2013
    typ, data = con.search(None, '(BEFORE {0})'.format(before_date))  # search pointer for msgs before before_date

    if data != ['']:  # if not empty list means messages exist
        for num in data[0].split():
            con.store(num, '+X-GM-LABELS', '\\Trash')
        con.expunge()
        con.close()
        con.logout()
    else:
        print("- Nothing to remove.")

    return