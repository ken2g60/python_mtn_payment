import requests
# change it to your api keys



def requesttopay(amount, currency, externalId, partyId, referenceId, token):

    
    try:
        req = requests.post("https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay", headers={
            
            'Authorization': 'Bearer ' + token,
            'X-Reference-Id': referenceId,
            'X-Target-Environment': 'sandbox',
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': "3c73b3a94f1e4a648fa167f40e290a25"
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
        return req.status_code
    except Exception as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(e)
