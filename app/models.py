from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_name = db.Column(db.String)
    email = db.Column(db.String)
    teacher_id = db.Column(db.Integer, ForeignKey('teachers.teacher_id'))
    
    
    #teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)  # ForeignKey to link to teachers

    # Define the relationship between Student and Teachers
    #teacher = db.relationship('Teachers', backref=db.backref('students', lazy=True))

class Class(db.Model):
    __tablename__ = 'class'
    class_id = db.Column(db.Integer, primary_key=True, nullable=False)
    course_title = db.Column(db.String)
    course_status = db.Column(db.String)
    student_id = db.Column(db.Integer, ForeignKey('student.student_id'))
    teacher_id = db.Column(db.Integer, ForeignKey('teachers.teacher_id'))

class Teachers(db.Model):
    __tablename__ = 'teachers'
    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    teacher_name = db.Column(db.String)
    role = db.Column(db.String)
    class_id = db.Column(db.Integer, ForeignKey('class.class_id'))
    
class Fee(db.Model):
    __tablename__ = 'fee'
    fee_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    fee_status = db.Column(db.String)
    student_id = db.Column(db.Integer, ForeignKey('student.student_id'))
    class_id = db.Column(db.Integer, ForeignKey('class.class_id'))


#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import Column, ForeignKey, Integer, String, Float
#from sqlalchemy.orm import relationship

#db = SQLAlchemy()

#class Teachers(db.Model):
    #__tablename__ = 'teachers'
    #teacher_id = db.Column(db.Integer, primary_key=True)
    #teacher_name = db.Column(db.String)
    #role = db.Column(db.String)
    #classes = relationship('Class', backref='teacher')

#class Class(db.Model):
   # __tablename__ = 'class'
    #class_id = db.Column(db.Integer, primary_key=True)
    #course_title = db.Column(db.String)
    #course_status = db.Column(db.String)
    #teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'))
    #students = relationship('Student', backref='class')

#class Student(db.Model):
    #__tablename__ = 'student'
    #student_id = db.Column(db.Integer, primary_key=True)
    #student_name = db.Column(db.String)
    #email = db.Column(db.String)
    #class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'))

#class Fee(db.Model):
    #__tablename__ = 'fee'
    #fee_id = db.Column(db.Integer, primary_key=True)
    #amount = db.Column(db.Float)
    #fee_status = db.Column(db.String)
    #student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))

