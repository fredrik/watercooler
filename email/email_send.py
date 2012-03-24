import smtplib  
import settings

server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)  

def go(emails):
    message = "From: %s\r\nTo: %s\r\nSubject: Hi! How are you today?\r\n\r\n"
    message += "Hello there %s!\nIts a lovley(rainy/cloudy etc, get from api?) day today and Im curious to know how you are feeling and what you are working on. Can you be a sport and send me back a email?\n\n\nExample email:\n\nI'm feeling glad\nI'm working on stuff today\n\n(If you are working on something with a friend do tell!) \nI'm working on some cool stuff today with @someone\n\nHave a good day!"
    
    for (person, email_to) in emails:
        server.sendmail(settings.EMAIL_USER, email_to, message % (settings.EMAIL_USER, email_to, person))
    server.quit()

if __name__ == '__main__':
    emails = [('Simon Johansson', settings.EMAIL_USER)]
    go(emails)
