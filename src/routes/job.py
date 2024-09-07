from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from ..database import dbSqlAlchemy as db
from ..models import JobModel
from ..models import JobSchema

blp = Blueprint('Job', __name__, description='Operations on jobs')

@blp.route('/jobs/<int:job_id>')
class Job(MethodView):
    def get(self, job_id):
        return "Read a job"
    
    def put(self, job_id):
        return "Update a job"
    
    def delete(self, job_id):
        return "Delete a job"
    
@blp.route('/jobs')
class JobList(MethodView):
    def get(self):
        return "Read all jobs"
    
    def post(self):
        if request.content_type == "application/json":
            return "Create a job with json"
        elif request.content_type == "text/csv":
            return "Create a job with csv"
        elif request.content_type == "text/plain":
            return "Create a job with text"
        return "You fail bro"
    
