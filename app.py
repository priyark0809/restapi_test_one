from flask import Flask,jsonify

todo = Flask("__name__")

#i want to store the list in dictionary form



@todo.route("/students-list")
def students_list():
    student =[
    {  
    "id": 1,    
    "student_name": "John",
    "student_age": 20,
    "email": "john@gmail.com"
    },
    {
        "id": 2,
    "student_name": "Jane",
    "student_age": 21,
    "email": "jane@gmail.com"
    },
    {
        "id": 3,
    "student_name": "Bob",
    "student_age": 22,
    "email": "bob@gmail.com"
    }
    ]
    return jsonify(student)

@todo.route('/student/get/<int:id>')
def student_get_by_id(id):
    
     print(id)
     return "i will get the student id"

if __name__ == "__main__":
    todo.run(
        host="127.0.0.1",
        port=5010,
        debug=True
    )


