from opensearchpy import OpenSearch

# Create an OpenSearch client instance
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    #http_auth=('admin', 'admin')
)

# Define an index and a search query
index = 'my_index'
query = {
    "query": {
        "match_all": {}
    }
}

# Perform a search operation
response = client.search(index=index, body=query)

# Print search results
print("Search results:")
for hit in response['hits']['hits']:
    print(hit['_source'])
