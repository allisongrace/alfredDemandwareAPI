# curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -uaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa -H "Cache-Control: no-cache"  -d 'grant_type=client_credentials' 'https://account.demandware.com/dw/oauth2/access_token'
# curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -uaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa -H "Cache-Control: no-cache"  -d 'grant_type=client_credentials' 'https://account.demandware.com/dw/oauth2/access_token'

import requests
from requests.auth import HTTPBasicAuth

# Lets get a token!!!!
user = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
password = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# data = {'grant_type':'client_credentials'}
data = [
  ('grant_type', 'client_credentials'),
]
headers = {'Cache-Control': 'no-cache',
           'Content-Type':'application/x-www-form-urlencoded'}
url = 'https://account.demandware.com/dw/oauth2/access_token'
response = requests.post(url=url, data=data, headers=headers, auth=HTTPBasicAuth(user, password))
content = json.loads(response.content.decode("utf-8"))
print("we have your token! ", content['access_token'])
token = content['access_token']


# Now lets call the metadata api!!!!!
# curl -X GET -H "Authorization: Bearer cb705672-2310-42f5-91b7-1efdf44e9155" https://sb1-web-brooks.demandware.net/s/-/dw/meta/v1/rest/data/v17_8
url = "https://sb1-web-brooks.demandware.net/s/-/dw/meta/v1/rest/data/v17_8"
headers = {"Authorization":"Bearer " + token,
        "Content-Type":"application/json"}
requests.get(url=url, headers=headers)


# nothing else seems to work :(

# POST https://hostname:port/dw/data/v17_8/product_search?site_id={String}
site_id="BrooksRunning"
# POST https://hostname:port/dw/data/v17_8/product_search?site_id={String}
# https://sb3-web-brooks.demandware.net/s/BrooksRunning/dw/shop/v17_8/products/03e15cf3b7f9ba9315509dfa3e
url = "https://sb3-web-brooks.demandware.net/s/BrooksRunning/dw/data/v17_8/product_search?site_id="+site_id
headers = {"Authorization":"Bearer " + token,
        "Content-Type":"application/json"}

data = {
    "query" : {
        "text_query": {
            "fields": ["name"],
            "search_phrase": "Launch"
        }
    },
    "select" : "(**)"
}
requests.post(url = url, data=data, headers=headers)


# get product attempt
# PUT https://hostname:port/dw/data/v17_8/products/{id}
product_id="03e15cf3b7f9ba9315509dfa3e"
url = "https://sb3-web-brooks.demandware.net/s/BrooksRunning/dw/data/v17_8/products/"+product_id
headers = {"Authorization":"Bearer " + token,
        "Content-Type":"application/json"}
requests.put(url=url, headers=headers)