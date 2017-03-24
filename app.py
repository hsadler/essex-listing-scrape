#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
from controllers.scraper import Scraper
from models.email import Email

import pprint
pp = pprint.PrettyPrinter(indent=4)


def scrape_and_email_report():

    # collect all apartment instances
    apartments = []
    for property_location, property_code in config.essex_properties.iteritems():

        # get apartment instances
        new_apts = Scraper.essex_listings_scrape(
            date='5-15-2017',
            property_location=property_location,
            property_code=property_code,
            unit_criteria=config.unit_criteria,
            rent_max_criteria=config.rent_max_criteria
        )

        # concatenating arrays
        apartments = apartments + new_apts

    # construct and send email
    email_body = '\n\n'.join([apt.get_formatted_string() for apt in apartments])

    email = Email(
        recipients=config.recipients,
        subject='Essex Apartment Report',
        body=email_body
    )
    email.send()
