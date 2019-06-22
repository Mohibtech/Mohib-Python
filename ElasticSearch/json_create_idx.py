from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

with open('sample.json') as json_file:  
    data = json.load(json_file)
    idnum = 1

    for custrec in data['CustomerMaster']:
        #print(p['CustomerKey'],p['CustomerID'],p['DWCustomerNo'],p['CustomerFirstName'],p['CustomerLastName'],p['CustomerEmail'])     
        
        doc = {
            'CustomerKey': custrec['CustomerKey'],
            'CustomerID': custrec['CustomerID'],
            'DWCustomerNo':      custrec['DWCustomerNo'],
            'CustomerFirstName': custrec['CustomerFirstName'],
            'CustomerLastName': custrec['CustomerLastName'],
            'CustomerEmail':custrec['CustomerEmail']
        }

        res = es.index(index="cust-merge", doc_type='cust', id=idnum, body=doc)
        #print(res['result'])CustomerKey
        idnum += 1

for idnum in range(20):
    res = es.get(index="cust-merge", doc_type='cust', id=idnum)
    print(res['_source'])
