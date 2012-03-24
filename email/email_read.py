import email.parser
import imaplib
from email.utils import getaddresses
from email.header import decode_header
import time
import sys
import settings

class Get_Emails(object):

    
    def __init__(self, usr='',pwd=''
                ,tag='CRM', read_tag='Test Loaded'):
        self._usr = usr
        self._pwd = pwd
        self._tag=tag
        self._read_tag=read_tag
        self._imapconn = self._get_connection()
    

    def _get_connection(self):
        try:
            imapconn = imaplib.IMAP4_SSL('imap.gmail.com', 993)
            imapconn.login(self._usr, self._pwd)
            imapconn.select('INBOX')
            return imapconn
        except imaplib.IMAP4.error:
            return None

    def _get_mails(self):
        if not self._imapconn:
            time.sleep(10)
            connection = self._get_connection()
            if not connection:
                sys.exit(-1)
            self.imapconn = connection
        search_ok, emails = self._imapconn.search(None, 'ALL')
        if len(emails[0]) > 0:
            fetch_ok, content = self._imapconn.fetch(','.join(emails[0].split(' ')),
                                '(UID INTERNALDATE BODY.PEEK[])')
            if fetch_ok != 'OK':
                print "\nError: failed to retrieve messages."
                sys.exit(-1)
            return (mail for mail in content if mail != ')')
        return []

    def _trash_email(self, id):
        #Archive that sucka
        self._imapconn.uid('STORE', id, '+FLAGS', '(\Deleted)')
        self._imapconn.uid('STORE', id, '+FLAGS', '(\Seen)')

    def _getFrom(self, data):
        return data.split('<')[0].strip()

    def get_mail(self):
        header_parser = email.parser.Parser()
        for extras, header in self._get_mails():
            mail_id = int(extras.split(' ')[2])
            parsed_mail = header_parser.parsestr(header)
            msg = {
                'from': self._getFrom(parsed_mail.get('from')),
                'date': parsed_mail.get('date'),
            }
            for part in parsed_mail.walk():
                if part.get_content_type() == 'text/plain':
                    msg['message'] = part.get_payload(decode=True)
                    self._trash_email(mail_id)
                    yield msg

if __name__ == '__main__':
    e = Get_Emails(usr=settings.EMAIL_USER, pwd=settings.EMAIL_PASSWORD)
    for mail in e.get_mail():
        print mail
        # Send to rabbit? Save directly to db?
