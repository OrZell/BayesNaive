from Manager import Manager
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/{name}')
async def root(name):
    manager = Manager(name)
    return manager.run()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)