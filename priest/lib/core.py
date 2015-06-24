'''
Core functions of Priest
'''

import msg_generator
import os, random
from utilities import *
from .. import __dir__
DATA_PATH = os.path.join(__dir__,'data')


def _customiser(command,msg,lang,font,pic):
    '''
        customise and return the message
    '''
    img_dir = os.path.join(DATA_PATH,'images/{0}'.format(command))
    # user forced a language
    if lang:
        if lang == 'en':
            pass
        else:
            msg = translate_message(msg,lang)
    # find the lang by the ip address
    else: 
        country_code = get_location()
        lang = get_language(country_code)
        msg = translate_message(msg,lang)
    # finally return the message
    if pic:
        file_list = next(os.walk(img_dir))[2]
        img = random.choice(file_list)
        img_path = os.path.join(img_dir,img)
        return prepare_image(msg,img_path,font)
    else:
        return msg


def morning(lang='',font='clearsans',pic=False):
    '''
        Generates a morning message
    '''
    msg = msg_generator.genMessage(os.path.join(DATA_PATH,'morning.data'))
    return _customiser('morning',msg,lang,font,pic)


def afternoon(lang='',font='clearsans',pic=False):
    '''
        Generates a afternoon message
    '''
    msg = msg_generator.genMessage(os.path.join(DATA_PATH,'afternoon.data'))
    return _customiser('afternoon',msg,lang,font,pic)


def evening(lang='',font='clearsans',pic=False):
    '''
        Generates a evening message
    '''
    msg = msg_generator.genMessage(os.path.join(DATA_PATH,'evening.data'))
    return _customiser('evening',msg,lang,font,pic)


def night(lang='',font='clearsans',pic=False):
    '''
        Generates a night message
    '''
    msg = msg_generator.genMessage(os.path.join(DATA_PATH,'night.data'))
    return _customiser('night',msg,lang,font,pic)


def now(lang='',font='clearsans',pic=False):
    '''
        Automatically generates a new message by getting all the info
        @param  lang  languages in which the message is to be translated
        @param  pic    whether to return picture or not
    '''
    # first get the time
    tz = get_timezone()
    time  = get_time(tz)
    command = get_command(time)
    retValue = globals()[command](lang,font,pic)
    return retValue



