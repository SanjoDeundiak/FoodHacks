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

sales_items_url = "http://metro.food-hacks.de/salesorder_items"

headers = {
'authorization': "Bearer {}".format(jwt_token),
'cache-control': "no-cache"
}
f = open('writefile.txt','w')
for i in range(1,70):
    sales_items_url_tmp = sales_items_url + "?customer_id=eq.Client_{:04d}&select=article_name".format(i)

    response = requests.request("GET", sales_items_url_tmp, headers=headers)

    json_array = json.loads(response.text)

    for json_object in json_array:

        print json_object['article_name'].encode('utf8')

        f.write(json_object['article_name'].encode('utf8'))
        f.write('\n')

    print i

f.close()