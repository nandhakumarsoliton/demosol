from fastapi import FastAPI
import subprocess
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    try:
        subprocess.call("./install_docker.sh", shell=True)
        return {"Status": "Installed Docker in App Service"}
    except Exception as e:
        return {"Status": "Failed to install Docker", "Error": str(e)}

if(__name__ == "__main__"):
    uvicorn.run(app)