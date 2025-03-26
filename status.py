from settings import *
from namastox import status
import json
from user import checkAccess

# GET STATUS of RA
@app.route(f'{url_base}{version}status/<string:ra_name>',methods=['GET'])
@app.route(f'{url_base}{version}status/<string:ra_name>/<int:step>',methods=['GET'])
@cross_origin()
def getStatus(ra_name, step=None):

    granted, access_result = checkAccess(ra_name,'read')
    if not granted:
        return access_result # this is the 403 JSON response

    success, data = status.action_status(ra_name, step, out='json')
    if success:
        return data
    else:
        return json.dumps(f'Failed to obtain status for {ra_name} with error: {data}'), 500, {'ContentType':'application/json'} 
