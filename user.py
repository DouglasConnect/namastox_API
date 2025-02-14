from settings import *
from flask import session
from namastox import manage
import json

def getUsername():
    try:
        user_name = session['user'].get('username', 'Unknown')
    except:
        user_name = 'generic'
    return user_name

    # return (session['user'].get('username', 'Unknown'))

def checkAccess(ra_name):
    try:
        user_name = session['user'].get('username', 'Unknown')
    except:
        user_name = 'generic'

    results = manage.action_privileges(ra_name, user_name)
    if not 'read' in results:
        return False, json.dumps(f'No permission to access {ra_name}'), 500, {'ContentType':'application/json'} 
    else:
        return True, user_name