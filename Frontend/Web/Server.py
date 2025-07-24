from Frontend.Manager import Manager
import uvicorn
from fastapi import FastAPI

app = FastAPI()

manager = Manager()
manager.checker()

@app.get('/')
def root():
    return 'Please Enter Data In The URL'

@app.get('/check')
async def Naive(data):
    return await manager.load_from_url(data)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)