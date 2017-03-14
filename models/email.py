#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Email Model

import config
import smtplib
import pprint

pp = pprint.PrettyPrinter(indent=4)



class Email():


    def __init__(self, recipients, subject, body):

        self.user = config.email_sender['email']
        self.password = config.email_sender['password']

        self.recipients = recipients
        self.subject = subject
        self.body = body


    def send(self):

        gmail_user = self.user
        gmail_pwd = self.password
        FROM = self.user
        TO = self.recipients if type(self.recipients) is list else [self.recipients]
        SUBJECT = self.subject
        TEXT = self.body

        # Prepare message
        message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (FROM, ", ".join(TO), SUBJECT, TEXT)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
        except:
            print 'failed to send mail'

        return self



