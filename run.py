from requests.exceptions import HTTPError
from utils.keys import apiuser_reference
from utils.requestPayment import requesttopay
from utils.keys import generate_token
from utils.verify import verify_payment
from utils.keys import genrate_transaction
import requests
import uuid
import json
from utils import literals



# testing numbers 
# https://momodeveloper.mtn.com/api-documentation/testing/
# change it to your api keys


try:
    userapi = str(uuid.uuid4())
    req = requests.post("https://sandbox.momodeveloper.mtn.com/v1_0/apiuser", 
                        headers={ 
                                'Content-Type': 'application/json',
                                'X-Reference-Id': userapi, 
                                'Ocp-Apim-Subscription-Key' : literals.Ocp_Apim_Subscription_Key},
                        json={'providerCallbackHost':'string'})
    print(req.text)
    
    apiKey = apiuser_reference(userapi)
    
    if apiKey != None:
        token = generate_token(userapi, apiKey)
        if token != None:
            # amount - 
            # currency - EUR (testing) 
            # externalId - generate random code 
            # partyId - 46733123452 
            # referenceId - uuid 
            #  token -> generated token 
            pay = requesttopay("1", "EUR", genrate_transaction(6), literals.partyId, userapi, token)
            print(pay)

            pay_status = verify_payment(userapi, token)

            print('payment status is----{}'.format(pay_status))
            
except requests.exceptions.RequestException as e:
    print(e.message)