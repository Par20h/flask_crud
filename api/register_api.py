from flask import render_template,redirect,request,jsonify,abort # type: ignore
from models.student_mod import Stu
from dbconn import db
from datetime import datetime

def register_api():
    data = request.get_json() or {}
    try:
        student = Stu(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            dob = datetime.strptime(data["dob"], "%Y-%m-%d").date()
        )
        db.session.add(student)
        db.session.commit()
        return jsonify(student.to_dict()), 201
    except KeyError:
        abort(400, "Missing required field")

def list_students_api():
    Students = Stu.query.all()
    print(Students)
    return jsonify([s.to_dict() for s in Students])  


def delete_api(id):
    Students = Stu.query.get_or_404(id)
    db.session.delete(Students)
    db.session.commit()
    return jsonify("Delete Successfully"),200

def update_api(id):
    data = request.get_json() or {}
    try:
        Students = Stu.query.filter_by(id=id).first()
        if not data:
            abort(404, "Student not found")

        Students.first_name = data["first_name"]
        Students.last_name = data["last_name"]
        Students.email = data["email"]
        Students.dob = datetime.strptime(data["dob"], "%Y-%m-%d").date()

        db.session.commit()
        return jsonify(Students.to_dict()), 200
    except KeyError:
        abort(400, "Missing required field")



        

