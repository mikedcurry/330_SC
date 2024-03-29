import openaq
from .openaq_py import *
from .models import DB, Record

API = openaq.OpenAQ()

def unity(l1, l2): # y'all need some unity...
    pals = [(l1[i], l2[i]) for i in range(0, len(l1))] # not perfect... might break.
    return pals

def get_values(city, parameter):
    status, body = API.measurements(city=city, parameter=parameter)
    datetime = [result['date']['utc'] for result in body['results']]
    value = [result['value'] for result in body['results']]
    list_unity = unity(datetime, value)
    return list_unity
