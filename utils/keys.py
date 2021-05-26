import requests, base64
from basicauth import encode
from random import randint

# change it to your api keys



    
def apiuser_reference(x_reference_id):
    try:
        req = requests.post("https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/" + x_reference_id + "/apikey", headers={
            'X-Reference-Id': x_reference_id,
            'Ocp-Apim-Subscription-Key ': "3c73b3a94f1e4a648fa167f40e290a25"
        })
        data = req.json()
        return data['apiKey']
    except Exception as err:
        print(err)
    except requests.exceptions.RequestException as e:
        print(e)


def generate_token(api_user, api_key):
    try:
        req = requests.post("https://sandbox.momodeveloper.mtn.com/collection/token/", headers={
            'Authorization': encode(api_user, api_key),
            'Ocp-Apim-Subscription-Key': "3c73b3a94f1e4a648fa167f40e290a25"
        })
        data = req.json()
        return data["access_token"]
    except Exception as err:
        print(err)
    except requests.exceptions.RequestException as e:
        print(e)


def genrate_transaction(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)