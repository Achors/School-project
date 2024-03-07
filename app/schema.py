from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import db,Student, Teachers

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student

class TeachersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teachers
        sqla_session = db.session