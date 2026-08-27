from fastapi import FastAPI

app = FastAPI(title="Todo API")


@app.get("/")
def root():
    return {"message": "Todo API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}