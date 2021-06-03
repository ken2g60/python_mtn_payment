import requests

# change it to your api keys
from utils import literals


def requesttopay(amount, currency, externalId, partyId, referenceId, token):

    
    try:
        req = requests.post("https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay", headers={
            
            'Authorization': 'Bearer ' + token,
            'X-Reference-Id': referenceId,
            'X-Target-Environment': 'sandbox',
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': literals.Ocp_Apim_Subscription_Key
        },
        json ={
            "amount": amount,
            "currency": currency,
            "externalId": externalId,
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": partyId
            },
            "payerMessage": "change me please",
            "payeeNote": "change me please"
            })
        return req.text
    except Exception as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(e)
