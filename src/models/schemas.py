from marshmallow import Schema, fields

class JobSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    
class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    
class EmploymentsRecordSchema(Schema):
    id = fields.Int(dump_only=True)
    employee_id = fields.Int(required=True)
    job_id = fields.Int(required=True)
    department_id = fields.Int(required=True)
    hire_date = fields.Date(required=True)

