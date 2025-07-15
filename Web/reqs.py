import requests

API_LINK = 'http://127.0.0.1:8000/1,1,1,1,1,-1,0,1,-1,1,1,-1,1,0,-1,-1,1,1,0,1,1,1,1,-1,-1,0,-1,1,1,1'
response = requests.get(API_LINK)
status = response.status_code
print(status)
if status == 200:
    print(response.json())