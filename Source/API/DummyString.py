import requests
import json
from collections import Counter

def best_choice(customer_id):
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
    sales_items_url_tmp = sales_items_url + "?customer_id=eq.Client_{:04d}&select=article_name".format(customer_id)

    response = requests.request("GET", sales_items_url_tmp, headers=headers)

    json_array = json.loads(response.text)

    string_list = list()

    for json_object in json_array:

        string_list.add(json_object['article_name'].encode('utf8'))

    mcommon = [ite for ite, it in Counter(string_list).most_common(3)]
    return mcommon

