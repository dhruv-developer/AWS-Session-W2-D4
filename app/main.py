from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message" : "Welcome to AWS Session Week 2 Day 4"
    }

@app.get("/about")
def about():
    return{
        "name" : "FASTAPI",
        "docker" : True
    }