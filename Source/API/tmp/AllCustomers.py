__author__ = 'wwwvi_000'
from InvoicesByCustomers import InvoicesByCustomers
from CustomerByCheck import CustomerByCheck


#list of customers
CustomerIDs = []
#list of lists of checks, (number of customers)*(a list of check IDs for each customer)
CustomerChecks = InvoicesByCustomers()


#for i in range(0,675):
#    print `i+1`
#    print CustomerChecks[i]

clusterInput = []
for i in range(len(CustomerChecks)):
    #find resulting vector for each customer, by list of his checks
    clusterInput.append(CustomerByCheck(CustomerChecks[i]))
