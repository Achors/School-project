from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import Student


class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student