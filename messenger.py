"""Module for emailing the scraped image as part of
the timesheet reminder. This modules sends the work
done by the scraper module."""

import configparser
import json
import os
import smtplib

from datetime import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(filename):
    """
    Function takes one argument--the name of the file created by
    the download_img() method which returns the name of the image
    file scraped and downloaded from the target page. It sends the
    program email with scraped jpeg as an attachment.  Email recipients
    are read in from the config file.

    It uses json for converting config objects to
    Python dictionary and list for passing as arguments for
    the emailing function.

    Note:  Users can manage the send email, password and target
    recipients by creating and editing a config file.
    """
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')
    # convert config item from string to dict to access values
    for key,value in config['Recipients'].items():
        # json parsing requires double quotes
        value = value.replace("'", '"')
        recipients_string = u'{}'.format(value)
        recipients_dict = json.loads(recipients_string)

    ##################### FOR TESTING ########################
    # tester email list
    for k,v in config['Email_List'].items():
        v = v.replace("'", '"')
        string = v
        test_list_dict = json.loads(string)

    test_list = [value for key,value in test_list_dict.items()]
    ##################### FOR TESTING ########################

    message = """ This is Gollandbot, your friendly timesheet reminder. I'm \
a bot. My job is to remind you to submit a completed timesheet to your \
supervisor. That's what I care abot.\n\n\
Because you know the time is ticking on this task, rather than send you \
an image of a ticking clock, instead I have grabbed and attached the most \
recent caption contest image from the NewYorker.\n\nEnjoy the image, \
hand in your timesheet today by 10:00am if you haven't already done so and, \
good luck with the caption contest.\n\t--Gollandbot"""

    sender = config['Email']['email_address']
    password = config['Email']['password']
    msg = MIMEMultipart()
    # live emails in below line
    #msg['To'] = [value for key,value in recipients_dict.items()]
    # remove test email list before deploying
    msg['To'] = ','.join(test_list)
    msg['From'] = sender
    msg['Subject'] = 'Timesheets Gollandbot : )'
    body = MIMEText(message)
    msg.attach(body)
    filepath = os.path.join('images',filename)
    #filepath = os.path.join('images','08-26-gollandbot-image.jpg')
    with open(filepath, 'rb') as file:
        payload = MIMEBase('application', 'octet-stream')
        payload.set_payload(file.read())
        encoders.encode_base64(payload)
        payload.add_header(
            'Content-Disposition', 'attachment; filename={}'.format(filepath.split('/')[1]))

    msg.attach(payload)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, password)

    # smtp protocol needs emails separated by comma to send to multiple recipients
    # if not separated by comma, the email will include all recipients in header
    # but will be sent only to first address in the list

    smtpObj.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    smtpObj.quit()
    day = dt.today().strftime('%A %b %d,%Y')
    time = dt.today().strftime('%-I:%M %p')
    print('Messages sent: {} at {}'.format(day,time))
