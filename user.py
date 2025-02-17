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

    # read access is checked allways    
    if not 'r' in results:
        return False, (json.dumps(f'Forbidden READ access to {ra_name}'), 403, {'ContentType':'application/json'})
    
    # if access checked is write and no permission is granted return error
    if access_type == 'write' and not 'w' in results:
        return False, (json.dumps(f'Forbidden WRITE access to {ra_name}'), 403, {'ContentType':'application/json'})

    return True, user_name
