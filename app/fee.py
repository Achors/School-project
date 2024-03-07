from flask import jsonify, Blueprint
from flask_restful import Api, Resource
from models import db, Fee
from schema import FeeSchema

fee_schema = FeeSchema()
fees_schema = FeeSchema(many=True)


fee_bp = Blueprint('fee_bp', __name__)
api = Api(fee_bp)


class FeeResource(Resource):
    def get(self, fee_id=None):
        if fee_id is None:
            fees = Fee.query.all()
            return jsonify(fees_schema.dump(fees))
        else:
            fee = Fee.query.get_or_404(fee_id)
            return jsonify(fee_schema.dump(fee))
        

api.add_resource(FeeResource, '/fees', '/fees/<int:fee_id>')

