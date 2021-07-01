import requests
import json

# We connect to the API using the below URL
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

# Replace DEMO_KEY below with your own key if you generated one.
api_key = "DEMO_KEY"

# Parameters to your API connection
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}

# Use the GET method to retrieve the data from the API
response = requests.get(endpoint, params=query_params)

# Print the JSON result from the response
print(response.text)

# Deserialize a JSON document to a Python object using this conversion table
responsejson = json.loads(response.text)

# Dump into a JSON file
with open(r'response.json', 'w', encoding='utf-8') as f:
    json.dump(responsejson, f, ensure_ascii=False, indent=4)