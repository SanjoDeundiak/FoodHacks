__author__ = 'wwwvi_000'

import json
import datetime
import pandas
from InvoiceParcing import InvoiceParcing
from functionOfTime import functionOfTime



def CustomerByCheck(CustomerChecks):


    json_data = open('data.txt').read()


    #data = json.loads(json_data)

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #CustomerID = "Client_0146"
    #CustomerChecks = ["Invoice_020076", "Invoice_020077"]
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



    sumprice = []
    datediff = []
    Checks = []
    for i in CustomerChecks:
        #get result vector for single check, a number in 0..1 for each cluster + date difference + sumprice
        tmp = InvoiceParcing(i)
        sumprice.append(tmp.pop())
        datediff.append(tmp.pop())
        Checks.append(tmp)

    #finding values of intermediary coefficients
    sumpricesum = 0
    for i in range(len(sumprice)):
        sumpricesum += sumprice[i]

    coefsum = 0
    sumpricenorm = sumprice
    for i in range(len(datediff)):
        sumpricenorm[i] = sumprice[i]/sumpricesum
        datediff[i] = functionOfTime(datediff[i])
        coefsum = coefsum + datediff[i]*sumpricenorm[i]

    #resulting vector
    customerVector = [0]*len(tmp)

    #for every cluster
    for j in range(len(tmp)):
        #for every check
        for i in range(len(datediff)):
            Checks[i][j] = Checks[i][j]*datediff[i]*sumpricenorm[i]
            customerVector[j] = customerVector[j] + Checks[i][j]
        customerVector[j] = customerVector[j]/coefsum


    return customerVector











    """
    #current date
    now = datetime.datetime.now().date()
        #add date to the vector
        datediff = now - checkdate
        Checks[i].append(datediff)
        #add price to the vector
        Checks[i].append(sumprice)
    """




    #for x in data:
    #    print x['invoice_id']





