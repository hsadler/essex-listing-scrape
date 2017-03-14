#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Scrape controller

import requests
import datetime

from models.email import Email
from models.apt_listing import AptListing

import pprint
pp = pprint.PrettyPrinter(indent=4)



class Scraper():


    @staticmethod
    def essex_listings_scrape():

        scrape_url = 'http://www.essexapartmenthomes.com/api/get-available/sfo1130/'

        date = str(datetime.date.today()).split('-')
        date = '-'.join([date[1], date[2], date[0]])

        res = requests.get(scrape_url + date)
        listings = res.json()

        # pp.pprint(listings)
        # print '==========================================================='

        filtered_listings = []

        # filter out the units that meet the criteria
        for unit_type in listings:
            if (unit_type['bed_bath'] == '1.5 Beds / 1 Bath'
            or unit_type['bed_bath'] == '2 Beds / 1 Bath'):
                for floor_plan in unit_type['floorplans']:
                    for unit in floor_plan['units']:
                        filtered_listings.append(unit)

        pp.pprint(filtered_listings)








