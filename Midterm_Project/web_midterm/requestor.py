import requests

response = requests.get(url="http://localhost:5028/animals")

print(response.status_code)
print(response.json())
print(response.headers)
