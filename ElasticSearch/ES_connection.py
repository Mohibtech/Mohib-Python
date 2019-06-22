import json
import requests
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

doc1 = {
    'author': 'Farooq',
    'text': 'Customer Merge',
    'timestamp': datetime.today().isoformat(),
}
doc2 = {
    'author': 'Umeed',
    'text': 'Reading Stories to Umar Farooq',
    'timestamp': datetime.today().isoformat(),
}

res = es.index(index="test-index", doc_type='tweet', id=1, body=doc1)
res2 = es.index(index="test-index", doc_type='tweet', id=2, body=doc2)

print(res['result'])

res = es.get(index="test-index", doc_type='tweet', id=2)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])

for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
