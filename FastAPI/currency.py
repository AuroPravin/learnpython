from fastapi import FastAPI
from pydantic import BaseModel
from forex_python.converter import CurrencyRates

app=FastAPI()

class Convertreq(BaseModel):
    source_curren:str
    target_curren:str
    amount:float

class Convertres(BaseModel):
    source_curren:str
    target_curren:str
    amount:float
    conv_amount:float

curren_rate=CurrencyRates()


@app.post("/convert/", response_model=Convertres)
def convert_currency(request:Convertreq):

    exchange_rate=curren_rate.get_rate(request.source_curren,request.target_curren)

    converted_amount=request.amount*exchange_rate


    response=Convertres(
        source_curren=request.source_curren,
        target_curren=request.target_curren,
        amount=request.amount,
        conv_amount=converted_amount
    )
    return