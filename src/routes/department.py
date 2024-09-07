from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from ..database import dbSqlAlchemy as db
from ..models import DepartmentModel
from ..models import DepartmentSchema

blp = Blueprint('Department', __name__, description='Operations on departments')

@blp.route('/departments/<int:department_id>')
class Department(MethodView):
    def get(self, department_id):
        return "Read a department"
    
    def put(self, department_id):
        return "Update a department"
    
    def delete(self, department_id):
        return "Delete a department"
    
@blp.route('/departments')
class DepartmentList(MethodView):
    def get(self):
        return "Read all departments"
    
    def post(self):
        if request.content_type == "application/json":
            return "Create a department with json"
        elif request.content_type == "text/csv":
            return "Create a department with csv"
        elif request.content_type == "text/plain":
            return "Create a department with text"
        return "You fail bro"
    
