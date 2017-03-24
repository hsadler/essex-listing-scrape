#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Scrape controller

import requests
import sys
from models.email import Email
from models.apt_listing import AptListing

import pprint
pp = pprint.PrettyPrinter(indent=4)



class Scraper():


    @staticmethod
    def essex_listings_scrape(date, property_location, property_code,
        unit_criteria=[], rent_max_criteria=float('inf')):

        # build scrape url
        base_url = 'http://www.essexapartmenthomes.com/api/get-available/'
        scrape_url = base_url + '/'.join([property_code, date])

        # get json from api call
        res = requests.get(scrape_url)
        listings = res.json()

        # filter out the units that meet the criteria
        filtered_listings = []
        for unit_type in listings:
            if unit_type['bed_bath'] in unit_criteria:
                for floor_plan in unit_type['floorplans']:
                    for unit in floor_plan['units']:
                        if unit['rent'] <= rent_max_criteria:
                            filtered_listings.append(unit)

        # collect apartment instances
        apartments = []
        for listing in filtered_listings:
            apartments.append(
                AptListing(
                    property_location=property_location,
                    baths=listing['baths'],
                    beds=listing['beds'],
                    rent=listing['rent'],
                    square_feet=listing['square_feet'],
                    amenities_display=listing['amenities_display'],
                    available_date=listing['available_date'],
                    apply_link=listing['apply_link']
                )
            )

        return apartments






