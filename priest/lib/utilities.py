'''
    Utility functions for fetching data from REST APIs
'''

import requests, goslate
import os
from PIL import Image, ImageFont, ImageDraw, time

def get_coordinates():
    '''
        Returns the lattitude & longitude pairs
    '''

def get_time(lattitude,longitude):
    '''
        Find the current time at the location pointed out by the lattitude and longitude
    '''


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


def prepare_image(msg,img_path,font):
    '''
        Prepare the image by writing text to it by using the supplied font
        @param  img  The image path
        @param  msg  The message need to be written on the image
        @param  font  The font to be used ( "the ttf path /data/fonts/clearsans.ttf")
    '''
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont(font,18)
    width,height = img.size
    # writing on the image
    draw.text((int(height*0.75),int(width/10.0)),
             'Sample text',(255,255,255),font=font)
    # wtf is to be done with the image
    path = os.getabspath('../data/user_data/{0}'.format(str( int(time.time()) )))
    img.save(path)
    return path


