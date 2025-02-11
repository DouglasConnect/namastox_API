from settings import *
from namastox import status
import json

def getUsername():
    return ('manuel')

# GET STATUS of RA
@app.route(f'{url_base}{version}status/<string:ra_name>',methods=['GET'])
@app.route(f'{url_base}{version}status/<string:ra_name>/<int:step>',methods=['GET'])
@cross_origin()
def getStatus(ra_name, step=None):
    user_name =  getUsername()
    success, data = status.action_status(ra_name, user_name, step, out='json')
    if success:
        return data
    else:
        return json.dumps(f'Failed to obtain status for {ra_name} with error: {data}'), 500, {'ContentType':'application/json'} 
