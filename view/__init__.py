from flask import Blueprint # type: ignore
from view.register import student_re,list_students,delete,update    
bp = Blueprint('auth',__name__)

bp.add_url_rule('/',view_func=student_re,endpoint='base',methods=['GET','POST'])
bp.add_url_rule('/register',view_func=student_re,endpoint='base',methods=['GET','POST'])
bp.add_url_rule('/list_students',view_func=list_students,endpoint='list_students',methods=['GET'])
bp.add_url_rule('/delete/<int:id>', view_func=delete,endpoint='delete',methods=['GET','POST'])
bp.add_url_rule('/update/<int:id>', view_func=update,endpoint='update',methods=['GET','POST'])