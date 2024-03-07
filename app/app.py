from flask import Flask
from models import db
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from student import student_bp
from flask_restful import Api
from teacher import GetAllTeacher,GetAllStudents,GetTeacherById,AddTeacher,UpdateTeacher,PartlyUpdateTeacher,DeleteTeacher
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
#get all teachers
api.add_resource(GetAllTeacher,'/get-all-teachers')  
#get all students
api.add_resource(GetAllStudents, '/get-all-students')
#get teacher by id
api.add_resource(GetTeacherById, '/get-teacher-by-id/<int:teacher_id>')
#add a new teacher
api.add_resource(AddTeacher, '/add-teacher')
#update teacher by id
api.add_resource(UpdateTeacher, '/update-teacher/<int:teacher_id>')

# Add routes for PartlyUpdateTeacher
api.add_resource(PartlyUpdateTeacher, '/partly-update-teacher/<int:teacher_id>')
#delete teacher by id
api.add_resource(DeleteTeacher, '/delete-teacher/<int:teacher_id>')

if __name__ == "__main__":
    app.run(debug=True)
