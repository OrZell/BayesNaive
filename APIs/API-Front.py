from FrontManager import FrontManager
from fastapi import FastAPI

app = FastAPI()

manager = FrontManager()
manager.checker()

@app.get('/')
def root():
    return 'Please Enter data In The URL'

@app.get('/check')
def naive(data):
    return manager.load_from_url(data)