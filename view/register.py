from flask import render_template,redirect,request # type: ignore
from models.student_mod import Stu
from dbconn import db

# def student_re():
#     if request.method == 'POST':
#         fname = request.form.get('fname')
#         lname = request.form.get('lname')
#         email= request.form.get('email')
#         dob= request.form.get("dob")

#         data = Stu(fname = fname , lname = lname ,email = email,dob = dob)
#         db.session.add(data)
#         db.session.commit()
#         return redirect('/list_students')
#     all_data = Stu.query.all()
#     return render_template('register.html',all_data = all_data)

def student_re():
    return render_template('register.html')


# def list_students():
#     students = Stu.query.all()
#     return render_template('list_students.html',students=students)  

def list_students():
    # students = Stu.query.all()
    return render_template('list_students.html')

def delete(id):
    data = Stu.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

# def update(id):
#     if request.method == "POST":
#         fname = request.form['fname']
#         lname = request.form['lname']
#         email = request.form['email']
#         dob = request.form['dob']

#         data = Stu.query.filter_by(id=id).first()
#         data.fname = fname
#         data.lname = lname
#         data.email = email
#         data.dob = dob
#         db.session.add(data)
#         db.session.commit()
#         return redirect('/register')

#     data = Stu.query.filter_by(id=id).first()
#     return render_template('update.html',data=data)

def update(id):
    data = Stu.query.filter_by(id=id).first()
    return render_template('update.html',data=data)