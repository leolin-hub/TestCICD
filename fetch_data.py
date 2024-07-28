import requests
import json

# 公開API的URL
url = 'https://api.example.com/data'

response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    data = response.json()
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
else:
    print(f"Failed to fetch data: {response.status_code}")
