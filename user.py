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

def checkAccess(ra_name, access_type):
    try:
        user_name = session['user'].get('username', 'Unknown')
    except:
        user_name = 'generic'

    results = manage.action_privileges(ra_name, user_name)
    
    code = {'read':'r', 'write':'w'}
    if not code[access_type] in results:
        return False, (json.dumps(f'Forbidden {access_type} access to {ra_name}'), 403, {'ContentType':'application/json'})
    else:
        return True, user_name
