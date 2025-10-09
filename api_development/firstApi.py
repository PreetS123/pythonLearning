from fastapi import FastAPI


app = FastAPI()

# localhost/create-user
# GET
# POST
# PUT
# DELETE


@app.get("/")
def index():
    return {"name": "First Data"}
