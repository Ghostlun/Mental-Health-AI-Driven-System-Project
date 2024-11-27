import requests

url = "http://127.0.0.1:5000/generate-advice"
payload = {
    "input": "I failed my exam and feel like I am going to always fail. What should I do?"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print("Response:", response.json())
