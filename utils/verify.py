import requests
# change it to your api keys
from utils import literals


def verify_payment(referenceId,token):
    
    try:
        req = requests.get("https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/" + referenceId, headers={
            'referenceId': referenceId,
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json',
            'X-Target-Environment': 'sandbox',
            'Ocp-Apim-Subscription-Key ': literals.Ocp_Apim_Subscription_Key
        })
        
        return req.text
    except Exception as e:
        print(e.message)