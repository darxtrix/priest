'''
Core functions of Priest
'''

import msg_generator
import os

DATA_PATH = os.path.join(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ),'data')


def morning():
    '''
        Generates a morning message
    '''
    return msg_generator.genMessage(os.path.join(DATA_PATH,'morning.data'))


def afternoon():
    '''
        Generates a afternoon message
    '''
    return msg_generator.genMessage(os.path.join(DATA_PATH,'afternoon.data'))


def evening():
    '''
        Generates a evening message
    '''
    return msg_generator.genMessage(os.path.join(DATA_PATH,'evening.data'))


def night():
    '''
        Generates a night message
    '''
    return msg_generator.genMessage(os.path.join(DATA_PATH,'night.data'))


