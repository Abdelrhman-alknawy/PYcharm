import requests

# Set the API endpoint URL
url = "https://api.poe.chat/gpt"

# Set the request headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Set the request data
data = {
    "input": "Hello, how are you?",
    "length": 50,
    "temperature": 0.7,
    "top_p": 1.0
}

# Send the request
response = requests.post(url, headers=headers, json=data)

# Check the response status code
if response.status_code == 200:
    # Parse the response data
    output = response.json()["output"]
    print(output)
else:
    print("Error:", response.status_code)