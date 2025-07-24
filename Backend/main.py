from BackendManager import BackendManager
from fastapi import FastAPI
import uvicorn

app = FastAPI()
BM = BackendManager()
BM.DoAll()

@app.get('/GetTheModel')
def GetTheModel():
    return BM.MainModel.GetTheModel()

@app.get('/AllRelevantColumns')
def AllRelevantColumns():
    return BM.MainModel.AllRelevantColumns

@app.get('/AllTablesLen')
def AllTablesLen():
    return BM.MainModel.AllTablesLen

@app.get('/LenOfPrimaryTable')
def LenOfPrimaryTable():
    return BM.MainModel.LenOfPrimaryTable

@app.get('/ExempleRow')
def ExempleRow():
    return BM.MainModel.ExempleRow

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)