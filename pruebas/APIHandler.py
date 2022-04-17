import datetime
import json
from hashlib import sha256

import requests

class APIHandler(object):
    def __init__(self):
       pass

    def sendRequest(self, dataRequest):
        URL = 'http://192.168.1.116:8071'
        USER = '1damX'
        PASS = '1234'
        passSHA256 = sha256(PASS.encode('utf-8')).hexdigest()
        minutes = str(datetime.datetime.now().minute)
        tokenString = USER + '/raspberrySemaforo1' + passSHA256 + minutes
        tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()

        response = requests.post(URL + '/raspberrySemaforo1',
                                 data=json.dumps(dataRequest),
                                 headers={"Content-Type": "application/json"},
                                 auth=(USER, tokenSHA256)).json()

        responseJSON = json.loads(response['response'])
        return responseJSON


