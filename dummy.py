from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    try:
        
        return {"Status": "Dummy Me running"}
    except Exception as e:
        return {"Status": "Failed to install Dummy me", "Error": str(e)}

if(__name__ == "__main__"):
    uvicorn.run(app)