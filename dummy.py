from fastapi import FastAPI

import uvicorn

dapp = FastAPI()

@dapp.get("/value")
def read_root():
    try:
        return {"Status": "Dummy Me running"}
    except Exception as e:
        return {"Status": "Failed to install Dummy me", "Error": str(e)}

