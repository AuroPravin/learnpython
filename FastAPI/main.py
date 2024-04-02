from fastapi import FastAPI,Path

app=FastAPI()

@app.get("/home1")
def read():
    return("It's working")

    


