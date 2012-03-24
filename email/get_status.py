from email_read import Get_Emails
import settings

emails = Get_Emails(usr=settings.EMAIL_USER, pwd=settings.EMAIL_PASSWORD)

def splitter(split_string, text):
    for line in (l.strip() for l in text.split('\n')):
        if split_string in line:
            return line.split(split_string)[-1].strip()
        
def im_feeling(ims):
    for im in ims:
        print im
        if 'feeling' in im:
            return im.split('feeling')[-1].strip()

def im_working_on(ims):
    # What are the person working with and with who?
    def collab_with(work):
        collabs = splitter('with @', work)
        if collabs:
            collabs = '@'+collabs # Evil hakk
            return [person.strip() for person in collabs.split(',')]
            
    for im in ims:
        if 'working on' in im:
            work = im.replace('working on ', '')
            people = collab_with(work)
            if people:
                work = work.split('with @')[0].strip()
            return (work, people)
        
def go():
    print "Fetching emails"
    for email in emails.get_mail():
        print email
        ims = [im.replace('\r\n',' ').strip() for im
               in email.get('message').split("I'm")
               if im.replace('\r\n', '').strip()]
        feeling = im_feeling(ims)
        working_on, working_with = im_working_on(ims)
        if not feeling:
            raise Exception('Eyh! You do have fealings right?')
        if not working_on:
            raise Exception('Eyh! You do have work to do, dont you?!')
        print "%s is feeling %s" % (email.get('from'), feeling)
        print "%s is working on %s" % (email.get('from'), working_on)
        if working_with:
            print "and the work is done with %s" % working_with
        
        data = {
            'from': email.get('from'),
            'email_addr': email.get('email'),
            'working_on': working_on,
            'working_with': working_with,
            'email': email.get('message')
        }
        print data

if __name__ == '__main__':
    go()
