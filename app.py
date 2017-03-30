#!/usr/bin/python
# -*- coding: utf-8 -*-

from controllers.scraper import Scraper
from models.apt_listing import AptListing
from models.email import Email

import config
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)



def scrape_and_email_report():

    # scrape
    apartments = get_listings_scrape()

    # gather apartment data as dictionaries
    apt_data = []
    for apt in apartments:
        apt_data.append(apt.__dict__)

    # save to daily data file
    with open('data/daily_apartments.json', 'w') as apt_file:
        json.dump(apt_data, apt_file, indent=4)

    # construct and send email
    email_body = '\n\n'.join([apt.get_formatted_string() for apt in apartments])

    email = Email(
        recipients=config.recipients,
        subject='Essex Apartment Report',
        body=email_body
    )
    email.send()



def poll_for_new_listings_and_email_report():

    # scrape
    apartments = get_listings_scrape()

    # TODO: MOVE A LOT OF THIS LOGIC TO A CONTROLLER

    # gather apartment data as dictionaries
    polled_apt_data = []
    for apt in apartments:
        polled_apt_data.append(apt.__dict__)

    # compare to daily saved data and gather new listings
    new_listings = []
    daily_listings = None
    with open('data/daily_apartments.json') as apt_file:
        daily_listings = json.load(apt_file)

    for listing in polled_apt_data:
        if listing not in daily_listings:
            new_listings.append(listing)


    if len(new_listings) > 0:

        # add any new listings in daily data file
        daily_listings = daily_listings + new_listings
        with open('data/daily_apartments.json', 'w') as apt_file:
            json.dump(daily_listings, apt_file, indent=4)

        # get new listings instances
        new_listings_instances = []
        for listing_dict in new_listings:
            new_listings_instances.append(
                AptListing(
                    property_location=listing_dict['property_location'],
                    baths=listing_dict['baths'],
                    beds=listing_dict['beds'],
                    rent=listing_dict['rent'],
                    square_feet=listing_dict['square_feet'],
                    amenities_display=listing_dict['amenities_display'],
                    available_date=listing_dict['available_date'],
                    apply_link=listing_dict['apply_link']
                )
            )

        # send urgent email with new listings
        email_body = '\n\n'.join(
            [apt.get_formatted_string() for apt in new_listings_instances]
        )

        email = Email(
            recipients=config.recipients,
            subject='URGENT: New Essex Listings Available!',
            body=email_body
        )
        email.send()

    else:
        print 'No new listings found...'



def get_listings_scrape():

    # collect all apartment instances
    apartments = []
    for property_location, property_code in config.essex_properties.iteritems():

        # get apartment instances
        new_apts = Scraper.essex_listings_scrape(
            date=config.target_move_in_date,
            property_location=property_location,
            property_code=property_code,
            unit_criteria=config.unit_criteria,
            rent_max_criteria=config.rent_max_criteria
        )

        # concatenating arrays
        apartments = apartments + new_apts

    return apartments


















