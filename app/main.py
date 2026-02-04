from fastapi import FastAPI
import subprocess   #  Remove this line wwhen its needed to showwcase it oke?

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Secure DevSecOps pipeline running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# 👇 Temporary insecure endpoint  for demo only
@app.get("/test")
def test():
    subprocess.call("ls", shell=True)
