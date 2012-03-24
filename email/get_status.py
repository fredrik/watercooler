from email_read import Get_Emails
import settings

emails = Get_Emails(usr=settings.EMAIL_USER, pwd=settings.EMAIL_PASSWORD)

def go():
    print "Fetching emails"
    for email in emails.get_mail():
        print email

if __name__ == '__main__':
    go()
