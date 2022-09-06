#import pandas as pd
import csv
import json
from fastapi import FastAPI


app = FastAPI()


def read_dict(file):
    with open("../src/test.json") as f:
        df = json.load(f)
    return df

@app.on_event("startup")
def startup_event():
    global full_dict
    full_dict = read_dict('test.json')

@app.get("/")
async def root():
    return {"message": full_dict}