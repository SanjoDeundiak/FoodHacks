import requests
import json

# -*- coding: UTF-8 -*-

url = "http://metro.food-hacks.de/rpc/login"
payload = "{ \"email\": \"metro@foodhacks.de\", \"pass\": \"RJbKtGCW2fyrG9hF\"}"
headers = {
'content-type': "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

# get response json
login_response = json.loads(response.text)

# get jwt token
jwt_token = login_response['token']

sales_items_url = "http://metro.food-hacks.de/salesorder_items?select=article_name"

headers = {
'authorization': "Bearer {}".format(jwt_token),
'cache-control': "no-cache"
}

offset = 0
limit = 10000

f = open('article_names.txt', 'a')

while True:

    headers['Range'] = `offset` + "-" + `(offset+limit-1)`

    response = requests.request("GET", sales_items_url, headers=headers)

    #sales_order_items = json.loads()

    if not response.text:
        break

    f.write(response.text.encode('utf8'))

    #for sales_order in sales_order_items:
    #article_names_set.add(sales_order['article_name'])

    offset += limit

    print offset

response = requests.request("GET", sales_items_url, headers=headers)

f.write(response.text.encode('utf8'))

f.close()