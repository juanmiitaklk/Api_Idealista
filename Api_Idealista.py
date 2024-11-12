import json
import requests
from requests.auth import HTTPBasicAuth

idealista_url = "https://api.idealista.com/oauth/token"

r = requests.post(idealista_url,
    auth=HTTPBasicAuth("*****************", "**************"),
    data={"grant_type": "client_credentials"}
)

token_response = json.loads(r.text)
token_value = token_response['access_token']

country = 'es'
center = '37.38283,-5.97317'
numPage = '1'
distance = '2000'
propertyType = 'homes'
operation = 'sale'
maxPrice = '160000'
minPrice = '80000'

api_url = 'https://api.idealista.com/3.5/es/search' + '?center=' + center + '&country=' + country + '&distance=' + distance + '&numPage=' + numPage + '&propertyType=' + propertyType + '&operation=' + operation + '&minPrice=' + minPrice + '&maxPrice=' + maxPrice
print(api_url)

r = requests.post(api_url, headers={"Authorization": "Bearer " + token_value})

js = json.loads(r.text)

print(json.dumps(js, indent=4))  
