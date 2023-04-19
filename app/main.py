from elasticsearch import Elasticsearch
import base64

# Create an instance of the Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Define an index name
index_name = 'my_index'

# Create an index with mappings
es.indices.create(index=index_name, ignore=400, body={
    'mappings': {
        'properties': {
            'name': {'type': 'text'},
            'age': {'type': 'integer'}
        }
    }
})

# Index a document
document = {
    'name': 'Mike Saragas',
    'age': 27
}
es.index(index=index_name, doc_type='_doc', document=document)

# Search for documents
query = {
    'query': {
        'match': {
            'name': 'Mike'
        }
    }
}
result = es.search(index=index_name, body=query)

# Print search results
print("Search results:")
for hit in result['hits']['hits']:
    print(f"Document ID: {hit['_id']}")
    print(f"Name: {hit['_source']['name']}")
    print(f"Age: {hit['_source']['age']}")
    print('---')

# Delete the index
es.indices.delete(index=index_name, ignore=[400, 404])
