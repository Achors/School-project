from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import Student, Class


class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student


class ClassSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Class