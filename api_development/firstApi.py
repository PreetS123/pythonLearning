from fastapi import FastAPI, Path


app = FastAPI()

# localhost/create-user
# GET
# POST
# PUT
# DELETE

students = {
    1: {
        "name": "Preeti",
        "age": 17,
        "class": "std 12"
    }
}


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):  # lt
    return students[student_id]


@app.get("/get-by-name/{name}")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"Data": "Not found"}
