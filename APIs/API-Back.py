from BackManager import BackManager
from fastapi import FastAPI
from AuxiFuncs import AuxiFuncs

app = FastAPI()

BM = BackManager()
BM.load_clean_train_test()

encode_dict = AuxiFuncs.encode_dict


@app.get('/GetTheModel')
def get_the_model():
    return encode_dict(BM.Trainer.get_the_model())

@app.get('/AllRelevantColumns')
def all_relevant_columns():
    return encode_dict(BM.Trainer.AllRelevantColumns)

@app.get('/AllTablesLen')
def all_tables_len():
    return encode_dict(BM.Trainer.AllTablesLen)

@app.get('/LenOfPrimaryTable')
def len_of_primary_table():
    return encode_dict(BM.Trainer.LenOfPrimaryTable)

@app.get('/ExempleRow')
def exemple_row():
    return encode_dict(BM.Trainer.ExempleRow)