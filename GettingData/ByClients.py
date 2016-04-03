import re
import json

number_of_customers = 70
offset = 1


f = open('file.txt')

filetext = f.read()

json_array = json.loads(filetext)

writef = open('writefile.txt', 'w')

i = 0

for json_obj in json_array:

    customer_id = json_obj['customer_id'].encode('ascii')

    customer_id_number = re.sub('Client_(0)*','',customer_id)

    if offset<=int(customer_id_number)<offset+number_of_customers:

        writef.write(json_obj['invoice_id'])
        writef.write('\n')

    i = i+1
    if i % 10000 == 0:
        print i

