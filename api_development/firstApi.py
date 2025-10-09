from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel


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


class Student(BaseModel):
    name: str
    age: int
    year: str


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):  # lt
    return students[student_id]


@app.get("/get-by-name/{student_id}")  # /get-by-name?name=preeti
def get_student(*, name: Optional[str] = None, test=int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error: ": "Student already exists"}
    students[student_id] = student
    return students
