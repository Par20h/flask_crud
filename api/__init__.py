from flask import Blueprint # type: ignore
from api.register_api import register_api,list_students_api,delete_api,update_api
api_bp = Blueprint('api',__name__)



api_bp.add_url_rule('/register_api',view_func=register_api,endpoint='register_api',methods=['POST','GET'])
api_bp.add_url_rule('/list_students_api',view_func=list_students_api,endpoint='list_studelist',methods=['GET'])
api_bp.add_url_rule('/delete_api/<int:id>', view_func=delete_api,endpoint='delete_api',methods=['DELETE'])
api_bp.add_url_rule('/update_api/<int:id>', view_func=update_api,endpoint='update_api',methods=['PUT'])

