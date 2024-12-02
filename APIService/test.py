import requests

url = "http://127.0.0.1:5000/test_api"

try:
    response = requests.post(url)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)