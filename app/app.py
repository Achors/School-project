from flask import Flask
from flask_restful import Api
from models import db, Teachers, Student
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from student import student_bp
from teacher import GetAllTeacher, GetAllStudents, GetTeacherById, AddTeacher, UpdateTeacher, PartlyUpdateTeacher, DeleteTeacher


app = Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db.init_app(app)
#db == SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Hello World!'

app.register_blueprint(student_bp)

api.add_resource(GetAllTeacher, '/teachers', endpoint='get_all_teachers')
api.add_resource(GetAllStudents, '/students', endpoint='get_all_students')
api.add_resource(GetTeacherById, '/teachers/<int:teacher_id>', endpoint='get_teacher_by_id')
api.add_resource(AddTeacher, '/teachers', endpoint='add_teacher')
api.add_resource(UpdateTeacher, '/teachers/<int:teacher_id>', endpoint='update_teacher')
api.add_resource(PartlyUpdateTeacher, '/teachers/partial/<int:teacher_id>', endpoint='partly_update_teacher')
api.add_resource(DeleteTeacher, '/teachers/<int:teacher_id>', endpoint='delete_teacher')

if __name__ == "__main__":
    app.run(debug=True)
