from BackendManager import BackendManager
from fastapi import FastAPI

app = FastAPI()
BM = BackendManager()
BM.DoAll()

import json

def encode_dict(d: dict) -> dict:
    def encode_key(k):
        return {"__key__": str(k), "__type__": type(k).__name__}

    def encode_item(obj):
        if isinstance(obj, dict):
            return {json.dumps(encode_key(k)): encode_item(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [encode_item(x) for x in obj]
        else:
            return obj

    return encode_item(d)


@app.get('/GetTheModel')
def GetTheModel():
    return encode_dict(BM.MainModel.GetTheModel())

@app.get('/AllRelevantColumns')
def AllRelevantColumns():
    return encode_dict(BM.MainModel.AllRelevantColumns)

@app.get('/AllTablesLen')
def AllTablesLen():
    return encode_dict(BM.MainModel.AllTablesLen)

@app.get('/LenOfPrimaryTable')
def LenOfPrimaryTable():
    return encode_dict(BM.MainModel.LenOfPrimaryTable)

@app.get('/ExempleRow')
def ExempleRow():
    return encode_dict(BM.MainModel.ExempleRow)