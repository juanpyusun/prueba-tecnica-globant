from flask import Flask

from .routes import JobBlueprint, DepartmentBlueprint, EmploymentRecordBlueprint

app = Flask(__name__)

def init_app(config):  
    #congiguration
    app.config.from_object(config)
    
    #blueprints
    app.register_blueprint(JobBlueprint)
    app.register_blueprint(DepartmentBlueprint)
    app.register_blueprint(EmploymentRecordBlueprint)
    return app