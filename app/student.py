from flask_restful import Api, Resource, reqparse
from flask import jsonify, Blueprint
from models import db, Student
from schema import StudentSchema



student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

student_bp = Blueprint('student_bp', __name__)
api = Api(student_bp)

class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get_or_404(student_id)
        return jsonify(student_schema.dump(student))

    def put(self, student_id):
        student = Student.query.get_or_404(student_id)
        parser = reqparse.RequestParser()
        parser.add_argument('student_name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('teacher_id', type=int)
        args = parser.parse_args()

        student.student_name = args.get('student_name', student.student_name)
        student.email = args.get('email', student.email)
        student.teacher_id = args.get('teacher_id', student.teacher_id)

        db.session.commit()
        res = jsonify(student_schema.dump(student))
        return res
    


api.add_resource(StudentResource, '/students/<int:student_id>')

