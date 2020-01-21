from requests.exceptions import HTTPError
from utils.keys import apiuser_reference
from utils.requestPayment import requesttopay
from utils.keys import generate_token
from utils.verify import verify_payment
from utils.keys import genrate_transaction
import requests
import uuid
import json


# testing numbers 
# https://momodeveloper.mtn.com/api-documentation/testing/
# change it to your api keys


try:
    userapi = str(uuid.uuid4())
    req = requests.post("https://sandbox.momodeveloper.mtn.com/v1_0/apiuser", 
                        headers={ 
                                'Content-Type': 'application/json',
                                'X-Reference-Id': userapi, 
                                'Ocp-Apim-Subscription-Key' : "4d1d6954ec0042e1924b5af8af61a823"}, 
                        json={'providerCallbackHost':'string'})
    print(req.json)
    
    apiKey = apiuser_reference(userapi)
    
    if apiKey != None:
        token = generate_token(userapi, apiKey)
        print(token)
        if token != None:
            # amount - 
            # currency - EUR (testing) 
            # externalId - generate random code 
            # partyId - 46733123452 
            # referenceId - uuid 
            #  token -> generated token 
            pay = requesttopay("2000", "EUR", genrate_transaction(6), "46733123452", userapi, token)
            print(pay)
            
except requests.exceptions.RequestException as e:
    print(e.message)