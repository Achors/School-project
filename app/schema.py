from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import Student, Class, Fee


class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student


class ClassSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Class


class FeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Fee