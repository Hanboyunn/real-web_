from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&apiKey=xxx&returnType=json"

    contents = requests.get(URL).text
    
    return { "messege": contents }

@app.get("/home")
def home():
    return {"messege": "Home!"}