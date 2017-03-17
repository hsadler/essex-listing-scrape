#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
from controllers.scraper import Scraper
from models.email import Email


# collect all apartment instances
apartments = []
for property_location, property_code in config.essex_properties.iteritems():

    # get apartment instances
    new_apts = Scraper.essex_listings_scrape(
        date='5-15-2017',
        appartment_criteria=config.appartment_criteria,
        property_location=property_location,
        property_code=property_code
    )

    apartments = apartments + new_apts


# construct and send email
email_body = '\n\n'.join([apt.get_formatted_string() for apt in apartments])

email = Email(
    recipients=config.recipients,
    subject='Essex Apartment Report',
    body=email_body
)
email.send()
