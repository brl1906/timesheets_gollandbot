"""Gollandbot program sends reminder emails to staff
about the necessary completion of their timesheets and
scrapes, downloads and attaches the NewYorker magazine
caption contest image as part of the email."""

import messenger
import scraper



if __name__ == '__main__':
    image_source = scraper.get_img()
    image_file = scraper.download_img(src=image_source)
    messenger.send_email(image_file)
