from Manager import Manager
import uvicorn
from fastapi import FastAPI

app = FastAPI()

manager = Manager()
manager.run()

@app.get('/')
def root():
    return 'Please Enter Data To URL as /check?data=...'

@app.get('/check')
async def Naive(data):
    return manager.load_from_url(data)

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)