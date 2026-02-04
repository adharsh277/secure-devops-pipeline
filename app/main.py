from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Secure DevSecOps pipeline running"}

@app.get("/health")
def health():
    return {"status": "ok"}
