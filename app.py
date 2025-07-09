from flask import Flask  
from view import bp as student_register
from api import api_bp as studetn_list
from config import Config
import dbconn
from dbconn import db
from models.student_mod import Stu


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = Config.SQLALCHEMY_ECHO

dbconn.init_app(app)
app.register_blueprint(student_register)
app.register_blueprint(studetn_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True,port=4000)