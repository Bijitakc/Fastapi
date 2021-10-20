from fastapi import FastAPI

#creating an instance of the fastapi object
app = FastAPI()

@app.get("/")
def index():
    return {name:"sdfved"}

