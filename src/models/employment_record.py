from database import dbSqlAlchemy as db

class EmploymentRecordModel(db.Model):
    __tablename__ = 'employment_records'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    
    def __repr__(self):
        return f'<EmploymentRecord:
                    <Employee: {self.name}>, 
                    <Date: {self.date}>, 
                    <Department: {self.department_id}>, 
                    <Job: {self.job_id}>>'