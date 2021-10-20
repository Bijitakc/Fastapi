from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#creating an instance of the fastapi object
app = FastAPI()

students = {
    1:{
        "name" : "john" ,
        "age"  : 19 ,
        "year" : "12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

@app.get("/")
def index():
    return {"name" :"sdfved"}


#path can specify the description and the value's requirements like greater than 0
@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(None, description="The id of the student you want to view", gt=0)):
    try:
        students[student_id]
        return students[student_id]
    except Exception :
        return { "message" : "student doesn't exist."}


#query parameter
#to add a optional parameter before queryparameter add * like below
@app.get("/get-by-name")
def get_by_name( *, name : Optional[str] = None):
    name = name.lower()
    for student_id in students:
        if students[student_id]["name"].lower() == name :
            return students[student_id]
    return {"Data" : "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error" : "Student exists"}
    
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id:int, student: UpdateStudent):
    if student_id not in students :
        return {"Error":"Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/de;ete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    del students[student_id]
    return {"Message": "Deleted"}

