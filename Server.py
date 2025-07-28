from Manager import Manager
from fastapi import FastAPI

app = FastAPI()

manager = Manager()
manager.run()

@app.get('/')
def root():
    return 'Please Enter Data To URL as /check?data=...'

@app.get('/check')
async def naive(data):
    return manager.load_from_url(data)