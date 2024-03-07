from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import db,Student, Class, Fee,Teachers


class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student


class ClassSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Class


class FeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Fee
class TeachersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teachers
        sqla_session = db.session