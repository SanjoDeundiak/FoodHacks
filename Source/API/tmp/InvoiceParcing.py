from pandas import DataFrame
from pandas import read_csv
import json
import datetime
import pandas as pd


#def InvoiceParcing(InvoiceInput):
InvoiceInput = 'Invoice_070787'
checkdate = 0
Grisha = read_csv('Grisha.csv',sep = ',',names=['name','ClusterName'])

with open('test.txt') as data_file:
    data = json.load(data_file)
    i=0
df = DataFrame(columns = ('name','price'))
for InvoiceCount in data:
    if (InvoiceInput == InvoiceCount['invoice_id']):
        df.loc[i]=[InvoiceCount['article_name'],InvoiceCount['turnover_inc_vat']*InvoiceCount['amount']]
        checkdate = InvoiceCount['order_date']
    i+=1
"""for x in df:
    for y in Grisha:
        if (x['name'] == y['name']):
            x['name']= y['ClusterName']

print df
"""

for index, row in df.iterrows():
   tmp = df[df.name == row.name].sum('price')
   df = df[df.name != row.name]
   df.merge(tmp,on= "name")

#df2 = pd.concat([df['name'], Grisha['name']], axis=1, keys=['df', 'Grisha'])

df1 = pd.merge(df,Grisha,on ='name', how= 'inner')

df1 = df1.sort('name');

print df1

a = [0 for x in range(Grisha['ClusterName'].max()+2)]


#for i in df['name']:
for i in range(len(a)):
    tmp9 = df['price']
    tmp10 = df['price'].sum()
    a[i]= df['[price']/df['price'].sum
    a[Grisha['ClusterName'].max() + 1] = datetime.datime.now().date() - checkdate
    a[Grisha['ClusterName'].max()+2]=df['price'].sum