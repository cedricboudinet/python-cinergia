'''
Cinergia: python library for control and monitoring of cinergia electronic load
-------------------------------------------------------------------------------

Released under the LGPL license
'''

__version__ = '0.9.0'
__author__ = "Cedric Boudinet"


def IQ21toFloat(Var):
    '''
    Converts 32 bits fixed point real number with 21 fractional bits
    into a floating point value
    '''
    if (Var > (0x1 << 31)):
        Var = Var - (0x1 << 32)
    return (1.0 * Var)/(0x1 << 21)


def IQ10toFloat(Var):
    '''
    Converts 32 bits fixed point real number with 10 fractional bits
    into a floating point value
    '''
    if Var > (0x1 << 31):
        Var = Var - (0x1 << 32)
    return (1.0 * Var) / (0x1 << 10)


def FloatToIQ21(Var):
    '''
    Converts floating point value into a
    32 bits fixed point real number with 21 fractional bits
    '''
    if Var < 0:
        Var = (Var * (0x1 << 21)) + (0x1 << 32)
    else:
        Var = Var * ((0x1 << 21))
    return int(Var)


def FloatToIQ10(Var):
    '''
    Converts floating point value into a
    32 bits fixed point real number with 10 fractional bits
    '''
    if Var < 0:
        Var = (Var * (0x1 << 10)) + (0x1 << 32)
    else:
        Var = Var * (0x1 << 10)
    return int(Var)
