'''
    Utility functions for fetching data from REST APIs
'''

import requests, goslate
import os, pytz, datetime, time
from PIL import Image, ImageFont, ImageDraw
import textwrap

def get_command(t):
    '''
        return the command to be used based on the current time
    '''
    if t < 43200 and t > 18000:
        command = 'morning'
    elif t > 43200 and t < 61200:
        command = 'afternoon'
    elif t > 61200 and t < 72000:
        command = 'evening'
    else:
        command = 'night'

    return command


def get_timezone():
    '''
        Returns the timezone info
    '''
    URL = 'http://www.telize.com/geoip'
    resp = requests.get(URL)
    return resp.json()['timezone']


def get_time(timezone):
    '''
        Return the current time in seconds at the location by using the timezone
    '''
    tz = pytz.timezone(timezone)
    curr_time = datetime.datetime.now(tz)
    (h,m,s) = curr_time.strftime('%H-%M-%S').split('-')
    return (int(h)*3600 + int(m)*60 + int(s))


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
    width,height = img.size
    lines = textwrap.wrap(text=msg,width=30)
    text_height = 0
    # writing on the image
    font_path = os.path.abspath('../data/fonts/{0}'.format(font+'.ttf'))
    font = ImageFont.truetype(font_path,16)
    for line in lines:
        draw.text((int(width/12.0),int(height*0.70)+text_height),
                 line,(255,255,255),font=font)
        text_height += font.getsize(line)[1]
    path = os.path.abspath('../user_data/{0}.jpg'.format(str( int(time.time()) )))
    img.save(path)
    return path


