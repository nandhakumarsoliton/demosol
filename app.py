from fastapi import FastAPI
import subprocess
import uvicorn
import requests
from fastapi import FastAPI
from dummy import dapp

app = FastAPI()

@app.get("/")
def read_root():
    try:

        uvicorn.run(dapp, host="127.0.0.1", port=9080)

        return {"Status": "App started in 9080"}
    except Exception as e:
        return {"Status": "Failed!", "Error": str(e)}
        

@app.get("/get")
def root():
    try:

        response = requests.get("http://127.0.0.1:9080/value")
        value = response.json()

        print(value)

        return value
    except Exception as e:
        return {"Status": "Failed!", "Error": str(e)}
        


if(__name__ == "__main__"):
    uvicorn.run(app)