'''
    Utility functions for fetching data from REST APIs
'''

import requests, goslate
import os

def get_location():
    ''' 
        Get the location from the IP address
    '''
    URL = 'http://www.telize.com/geoip'
    resp = requests.get(URL)
    return resp.json()['country_code']


def get_language(country_code):
    '''
        Get laguage code for a given country code
    '''
    api_key = os.getenv('X_Mashape_Key')
    if not api_key:
        raise Exception('X_Mashape_Key not found in the list of environment variables')
    else:
        URL = 'https://restcountries-v1.p.mashape.com/alpha/' + country_code
        headers = {'X-Mashape-Key' : api_key,'Content-Type' : 'application/json'}
        resp = requests.get(URL,headers=headers)
        return resp.json()['languages'][0]


def translate_message(msg,language_code):
    '''
        Translates the message from 'en' to the supplied language_code
    '''
    gs = goslate.Goslate()
    return gs.translate(msg,language_code)

