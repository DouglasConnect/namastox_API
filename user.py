from settings import *
from flask import session

def getUsername():
    try:
        user_name = session['user'].get('username', 'Unknown')
    except:
        user_name = 'generic'

    # return (session['user'].get('username', 'Unknown'))
    return (user_name)