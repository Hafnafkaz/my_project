from fastapi import FastAPI

app = FastAPI()  # Ensure this line is present to create the FastAPI instance

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
 

