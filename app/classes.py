from flask_restful import Api, Resource, reqparse
from flask import jsonify, Blueprint
from models import db, Class
from schema import ClassSchema


class_schema = ClassSchema()
classes_schema = ClassSchema(many=True)

class_bp = Blueprint('class_bp', __name__)
api = Api(class_bp)

class ClassResource(Resource):
    def get(self, class_id=None):
        if class_id is None:
            classes = Class.query.all()
            return jsonify(classes_schema.dump(classes))
        else:
            classed = Class.query.get_or_404(class_id)
            return jsonify(class_schema.dump(classed))
        

api.add_resource(ClassResource, '/classes', '/classes/<int:class_id>')