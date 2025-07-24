import requests

API_LINK = 'http://127.0.0.1:8001/check?data='
def Reqs(resource):
    url = API_LINK + resource
    response = requests.get(url)
    status = response.status_code
    if status == 200:
        return response.json()
    else:
        return 'Hello'


print(Reqs('1,1,1,1,1,-1,0,1,-1,1,1,-1,1,0,-1,-1,1,1,0,1,1,1,1,-1,-1,0,-1,1,1,1'))