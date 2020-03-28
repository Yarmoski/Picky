from __future__ import print_function

import os
import random
import argparse
import requests
import sys
import urllib
from urllib.parse import quote

from flask import url_for


API_KEY= os.environ.get('YELP_API_KEY') #Yelp Fusion API key goes here

#Constant path variables, used for concatenation
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

#Variables used for Yelp query
DEFAULT_TERM = random.choice(['food', 'restaurant','casual dining', 'eat', 'good dining'])
SEARCH_LIMIT = 20


#Thank you to Yelp.com for starter code!

def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print('Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, term, location, offset=0):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'offset': offset,
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(term, location, offset):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location, offset)

    businesses = response.get('businesses')

    if not businesses:
        print('No businesses for {0} in {1} found.'.format(term, location))
        return None
    
    #Returns list of businesses
    return businesses

def business_info(businesses, number):
    """returns the first photo url and the yelp url of specified business
    Args:
        businesses(list): List of businesses from query
        number(int): Number of business in list that should be collected from
    """
    placeholder_img = url_for('static', filename='images/not_found_v2.png')

    business_id = businesses[number]['id'] #returns ID of business

    response = get_business(API_KEY, business_id)
    photos = response.get('photos') #photos is now a list of 3 photo urls of the business

    url = response.get('url') #url is now the url of the yelp page of the business

    #If the photos are valid, return one. Else, return placeholder.
    if photos != None and len(photos) >= 2:
        photo_number = random.randint(0, 1)
        return [photos[photo_number], url]
    return [placeholder_img, url]

def execute(place, term):
    """returns a list of businesses with the specified search term and location
    Args:
        place(str): location input
    """

    if term == "":
        term = DEFAULT_TERM

    parser = argparse.ArgumentParser()

    random_offset = random.randint(31, 60)

    parser.add_argument('-q', '--term', dest='term', default=term, type=str)
    parser.add_argument('-l', '--location', dest='location', default=place, type=str)
    parser.add_argument('-o', '--offset', dest='offset', default=random_offset, type=int)

    input_values = parser.parse_args()
    #print(input_values)

    #add the first page of results to businesses
    businesses = query_api(input_values.term, input_values.location, 0)
    businesses2 = query_api(input_values.term, input_values.location, input_values.offset)



    #if the businesses2 list is not empty, add it onto businesses
    if businesses2:
        businesses = businesses + businesses2

    return businesses
   

