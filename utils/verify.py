import requests
# change it to your api keys


def verify_payment(amount,currency,externalId,partyId,referenceId,token):
    
    try:
        req = requests.get("https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/" + referenceId, headers={
            'referenceId': referenceId,
            'Authorization': 'Basic ' + token,
            'Content-Type': 'application/json',
            'X-Target-Environment': 'sandbox',
            'Ocp-Apim-Subscription-Key ': '4d1d6954ec0042e1924b5af8af61a823'
        },
        json={
            'amount': amount,
            'currency': currency,
            'externalId': externalId,
            'payer': {
                'partyIdType': 'MSISDN',
                'partyId': partyId
            },
            'payerMessage': 'Payment',
            'payeeNote' : 'refeee mtn'
        })
        
        return req.status_code
    except Exception as e:
        print(e.message)