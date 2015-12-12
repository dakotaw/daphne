#!/usr/bin/env python

import requests
import ConfigParser
import smtplib
import os

def get_freddie_type():
    """
    Grabs the text from the MailChimp Reply All page and scrapes for the
    type of Freddie available on the page. Returns the name as unicode.
    """
    url = ('http://mailchimp.com/replyall')
    response = requests.get('http://mailchimp.com/replyall')
    page_html = response.text
    div_tag = "<h1 class=\'giveaway-title kern\'>"
    first_split = page_html[page_html.find(div_tag) + len(div_tag) : ]
    freddie_type = first_split[ : first_split.find('<')]

    return freddie_type


def send_email(from_email, from_pass, to_email, subj, msg):
    """
    Sends an email from the given credentials' gmail account.
    """
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(from_email, from_pass)

    fr = "From: %s" % from_email
    to = "To: %s" % to_email
    email_msg = '\r\n'.join([fr, to, subj, "", msg])
    
    server.sendmail(from_email, to_email, email_msg)
    server.quit()


def main():
    
    config = ConfigParser.ConfigParser()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    
    config.readfp(open(os.path.join(dir_path, 'daphne.cfg'), 'r'))
    email_user = config.get('Email', 'user')
    email_password = config.get('Email', 'password')
    to_email = config.get('Email', 'to_email')

    current_freddie = config.get('Freddie', 'current')
    new_freddie = get_freddie_type()

    if new_freddie != current_freddie:
        send_email(from_email=email_user,
            from_pass=email_password,
            to_email=to_email,
            subj = "Subject: ALERT! NEW FREDDIE AVAILABLE",
            msg="""ALERT: New Freddie available! Claim at this link: 
            http://mailchimp.com/replyall/""")
        current_freddie = new_freddie

    else:
        print 'No new Freddie.'

    config.set('Freddie', 'current', current_freddie)
    config.write(open('daphne.cfg', 'w'))


if __name__ == '__main__':
    main()

