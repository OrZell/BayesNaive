from BackManager import BackManager
from fastapi import FastAPI
from AuxiFuncs import AuxiFuncs
import uvicorn

app = FastAPI()

BM = BackManager()
BM.LoadTrainTest()

encode_dict = AuxiFuncs.encode_dict


@app.get('/GetTheModel')
def get_the_model():
    return encode_dict(BM.Trainer.get_the_model())

@app.get('/AllRelevantColumns')
def AllRelevantColumns():
    return encode_dict(BM.Trainer.AllRelevantColumns)

@app.get('/AllTablesLen')
def AllTablesLen():
    return encode_dict(BM.Trainer.AllTablesLen)

@app.get('/LenOfPrimaryTable')
def LenOfPrimaryTable():
    return encode_dict(BM.Trainer.LenOfPrimaryTable)

@app.get('/ExempleRow')
def ExempleRow():
    return encode_dict(BM.Trainer.ExempleRow)