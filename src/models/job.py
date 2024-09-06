from database import dbSqlAlchemy as db

class JobModel(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Job {self.name}>'