import json
import re


invoices_list = list()

for i in range(0,675):
    invoices_list.append(list())

f = open('salesorders.txt')

json_string = f.read()

json_array = json.loads(json_string)

for json_obj in json_array:
    customer_id = json_obj['customer_id'].encode('ascii')

    customer_number = int(re.sub('Client_(0)*','',customer_id))

    invoices_list[customer_number-1].append(json_obj['invoice_id'])

for i in range(0,675):
    print `i+1`
    print invoices_list[i];

