import requests
import json

# Configure API request
endpoint = "https://developer.nps.gov/api/v1/alerts?"
HEADERS = {"X-Api-Key": "HYUlpoRkuv22ZxqHSRIVpFWQi75wMGxN1CAg6Kfd"}
params = {"parkCode": "yell"}
response = requests.get(endpoint, headers=HEADERS, params=params)
data = response.text
json_data = json.loads(data)
print(json_data)
