from fastapi import FastAPI
import subprocess   # 👈 add this line

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Secure DevSecOps pipeline running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# 👇 Temporary insecure endpoint (for DevSecOps demo)
@app.get("/test")
def test():
    subprocess.call("ls", shell=True)
