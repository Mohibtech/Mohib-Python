import json
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

######## Simple example of querying Elasticsearch creating REST requests ############

def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "content": term
            }
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results


def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['content']))


def create_doc(uri, doc_data={}):
    """Create new document."""
    query = json.dumps(doc_data)
    response = requests.post(uri, data=query)
    print(response)


if __name__ == '__main__':
    uri_search = 'http://localhost:9200/test/articles/_search'
    uri_create = 'http://localhost:9200/test/articles/'

    # results = search(uri_search, "fox")
    # format_results(results)

    create_doc(uri_create, {"content": "The fox!"})
    results = search(uri_search, "fox")
    #format_results(results)
