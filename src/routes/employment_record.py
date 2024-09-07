from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from ..database import dbSqlAlchemy as db
from ..models import EmploymentRecordModel
from ..models import EmploymentRecordSchema

blp = Blueprint('Employment Record', __name__, description='Operations on employmnt records')

@blp.route('/employment-records/<int:employment_record_id>')
class EmploymentRecord(MethodView):
    def get(self, employment_record_id):
        return "Read a employment record"
        
    def put(self, employment_record_id):
        return "Update a employment record"
    
    def delete(self, employment_record_id):
        return "Delete a employment record"
    
@blp.route('/employment-records')
class EmploymentRecordList(MethodView):
    def get(self):
        return "Read all employment records"
    
    def post(self):
        if request.content_type == "application/json":
            return "Create a employment records with json"
        elif request.content_type == "text/csv":
            return "Create a employment records with csv"
        elif request.content_type == "text/plain":
            return "Create a employment records with text"
        return "You fail bro"
    
