import requests
# change it to your api keys


def verify_payment(referenceId,token):
    
    try:
        req = requests.get("https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/" + referenceId, headers={
            'referenceId': referenceId,
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json',
            'X-Target-Environment': 'sandbox',
            'Ocp-Apim-Subscription-Key ': '3c73b3a94f1e4a648fa167f40e290a25'
        })
        
        return req.text
    except Exception as e:
        print(e.message)