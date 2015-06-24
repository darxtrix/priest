'''
            _           _   
 _ __  _ __(_) ___  ___| |_ 
| '_ \| '__| |/ _ \/ __| __|
| |_) | |  | |  __/\__ \ |_ 
| .__/|_|  |_|\___||___/\__|
|_|                         

Generate wishes from your command line with full customization.

Usage:
======

>>> from priest import morning
>>> morning()
    # => Generates a morning message in your native language

Flexibility :
-------------

>>> morning(lang='en',pic=True)
    # => Generates a picture message in English language

Now :
-----

>>> from priest import now
>>> now()
    # => Automatically gets the timezone and predicts whether it is morning,afternoon,evening 
    #   or night and generates a message accordingly in your native language

For more : github.com/black-perl/priest


'''

import os

__dir__ = os.path.abspath(os.path.dirname(__file__))
__version__ = 0.1

from .lib.core import *