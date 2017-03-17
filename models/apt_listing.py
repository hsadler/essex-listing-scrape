#!/usr/bin/python
# -*- coding: utf-8 -*-

# Apartment Listing model

import pprint
pp = pprint.PrettyPrinter(indent=4)



class AptListing():


    def __init__(
        self,
        property_location,
        baths,
        beds,
        rent,
        square_feet,
        amenities_display,
        available_date,
        apply_link
    ):
        self.property_location = property_location
        self.beds = beds
        self.baths = baths
        self.rent = rent
        self.square_feet = square_feet
        self.amenities_display = amenities_display
        self.available_date = available_date
        self.apply_link = apply_link


    def get_formatted_string(self):

        parts = [
            self.property_location,
            'beds: ' + str(self.beds),
            'baths: ' + str(self.baths),
            'rent: ' + str(self.rent),
            'square feet: ' + str(self.square_feet),
            'amenities: ' + str(self.amenities_display),
            'available: ' + str(self.available_date),
            'apply: ' + str(self.apply_link)
        ]

        return '\n'.join(parts)







