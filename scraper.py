"""
Program sends reminder emails to target list of employees to complete
their timesheets.  It mimics and enhances the manual emails of an existing
supervisor by getting the NewYorker magazine caption contest image and
attaching it to the reminder email, sending a light-hearted but memorable
reminder to recipients.
"""

import logging
import os
import requests
import smtplib
import sys

from bs4 import BeautifulSoup
from datetime import datetime as dt

def get_img():
    """
    Function parses newyorker site to get and return the image
    element for the caption contest.  It returns the src in img tag
    from the url: https://www.newyorker.com/cartoons/contest

    The request locates the img element in a div with the class:
    CaptionSubmissionStage__wrapper___2sPWK
    """
    url = 'https://www.newyorker.com/cartoons/contest'
    site_request = requests.get(url)

    try:
        if site_request.status_code == 200:
            content = site_request.content
            soup = BeautifulSoup(content, 'html.parser')

    except Exception as e:
        e_type, e_obj, e_traceback = sys.exc_info()
        print('Website request failed!\n')
        print('***{} is causing problems***'.format(str(e_traceback.tb_frame.f_code).split()[2]))
        print('Failure in object: {}\n'.format(e_traceback.tb_frame.f_code))
        print('Error type: {}\nError Message: {}\nError Location: line {}'.format(
            str(e_type).split("'")[1], e_obj, e_traceback.tb_lineno))

    try:
        # ensure target element search doesn't return None
        if not soup.find('div', class_='CaptionSubmissionStage__wrapper___2sPWK'):
            print('Target html element: CaptionSubmissionStage div not found!')

        else:
            caption_image_div = soup.find(
                'div', class_='CaptionSubmissionStage__wrapper___2sPWK')
            img = caption_image_div.img
            img_src = img['src']

    except Exception as e:
        e_type, e_obj, e_traceback = sys.exc_info()
        print('Website request failed!\n')
        print('***{} is causing problems***'.format(str(e_traceback.tb_frame.f_code).split()[2]))
        print('Failure in object: {}\n'.format(e_traceback.tb_frame.f_code))
        print('Error type: {}\nError Message: {}\nError Location: line {}'.format(
            str(e_type).split("'")[1], e_obj, e_traceback.tb_lineno))

    return img_src


def download_img(src):
    """
    Function scrapes and saves NewYorker caption contest
    image to file in directory labeled 'images'.
    It takes the image src in the img element returned from the
    get_img() function call.
    """
    if not src:
        filename = ''
        print('Image source not found')
    else:
        # request image source
        try:
            src_request = requests.get(src)
            src_request.raise_for_status()

        except Exception as e:
            e_type, e_obj, e_traceback = sys.exc_info()
            print('***{} is causing problems***'.format(str(e_traceback.tb_frame.f_code).split()[2]))
            print('Failure in object: {}\n'.format(e_traceback.tb_frame.f_code))
            print('Error type: {}\nError Message: {}\nError Location: line {}'.format(
                str(e_type).split("'")[1], e_obj, e_traceback.tb_lineno))

        # create directory for image
        try:
            os.makedirs('images',exist_ok=True)

        except Exception as e:
            e_type, e_obj, e_traceback = sys.exc_info()
            print('***{} is causing problems***'.format(str(e_traceback.tb_frame.f_code).split()[2]))
            print('Failure in object: {}\n'.format(e_traceback.tb_frame.f_code))
            print('Error type: {}\nError Message: {}\nError Location: line {}'.format(
                str(e_type).split("'")[1], e_obj, e_traceback.tb_lineno))

        # download image to file
        try:
            naming_convention = '{}-gollandbot-image'.format(dt.today().strftime('%m-%d'))
            file_extension = src.split('.')[-1]
            filename = '{}.{}'.format(naming_convention, file_extension)
            img_file = open(os.path.join('images', os.path.basename(filename)), 'wb')

            for chunk in src_request.iter_content(100000):
                img_file.write(chunk)
            img_file.close()
            print('Image downloaded to file')

        except Exception as e:
            e_type, e_obj, e_traceback = sys.exc_info()
            print('***{} is causing problems***'.format(str(e_traceback.tb_frame.f_code).split()[2]))
            print('Failure in object: {}\n'.format(e_traceback.tb_frame.f_code))
            print('Error type: {}\nError Message: {}\nError Location: line {}'.format(
                str(e_type).split("'")[1], e_obj, e_traceback.tb_lineno))

        return filename
