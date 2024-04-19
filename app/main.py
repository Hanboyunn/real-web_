from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&apiKey=JXK5Fo358W6N45ic5384WZ9V4e34F5LQRoc2TKxJ&returnType=json"

    contents = requests.get(URL).text
    
    return { "messege": contents }

@app.get("/home")
def home():
    return {"messege": "Home!"}