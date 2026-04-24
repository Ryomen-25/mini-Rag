from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return{
        "message": "Mini RAG is running"
    }


@app.get("/welcome")
def welcome():
    return{
        "message": "Hello"
    }