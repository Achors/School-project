from flask_restful import Api, Resource, reqparse
from flask import jsonify, Blueprint
from models import db, Student, Teachers
from schema import StudentSchema



student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

student_bp = Blueprint('student_bp', __name__)
api = Api(student_bp)

class StudentResource(Resource):
    def get(self, student_id=None):
        if student_id is None:
            students = Student.query.all()
            return jsonify(students_schema.dump(students))
        else:
            student = Student.query.get_or_404(student_id)
            return jsonify(student_schema.dump(student))
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student_name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('teacher_id', type=int, required=True)
        args = parser.parse_args()

        teacher = Teachers.query.filter_by(teacher_id=args['teacher_id']).first()
        if not teacher:
            
            teacher = Teachers(teacher_id=args['teacher_id'])
            db.session.add(teacher)
            db.session.commit()

        new_student = Student(
            student_name=args['student_name'],
            email=args['email'],
            teacher_id=args['teacher_id']
        )
        db.session.add(new_student)
        db.session.commit()

        return jsonify(student_schema.dump(new_student)), 201

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
    
    def delete(self, student_id):
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return '', 204


api.add_resource(StudentResource, '/students', '/students/<int:student_id>')

