from Manager import Manager
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return 'Please Enter Data In The URL'

@app.get('/check')
async def Naive(data):
    manager = Manager(data)
    return manager.run()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)