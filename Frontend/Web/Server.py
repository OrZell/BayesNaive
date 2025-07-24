from Frontend.Manager import Manager
from fastapi import FastAPI

app = FastAPI()

manager = Manager()
manager.checker()

@app.get('/')
def root():
    return 'Please Enter Data In The URL'

@app.get('/check')
def Naive(data):
    return manager.load_from_url(data)