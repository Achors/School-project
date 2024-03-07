from flask_restful import Api, Resource,request
from flask import jsonify
from models import db, Teachers,Student
from schema import TeachersSchema,StudentSchema



class GetAllTeacher(Resource):
    def get(self):
        schema=TeachersSchema()
        teachers = Teachers.query.all()
        results= schema.dump(teachers,many=True)
        return jsonify(results)
      
class GetAllStudents(Resource):
    def get(self):
        schema=StudentSchema()
        students=Student.query.all()
        results=schema.dump(students,many=True)
        return jsonify(results)
    
class GetTeacherById(Resource):
    def get(self, teacher_id):
        teacher_id=int(teacher_id)
        teacher=Teachers.query.filter_by(teacher_id=teacher_id).first()
        if teacher is None:
            return jsonify({"message":"No teacher found!"}) 
        schema=TeachersSchema()
        results = schema.dump([teacher], many=True)
        return jsonify(results)

class AddTeacher(Resource):
    def post(self): 
        schema=TeachersSchema()
        data=request.json
        new_teacher=Teachers(**data)
        #db.sessiom.add(new_teacher)
        db.session.commit()
        #return  jsonify(schema.dump(new_teacher)) 
        return("The teacher has been updated successfuly"),200 
class UpdateTeacher(Resource):
    def put(self,teacher_id):
        teacher_id=int(teacher_id)
        teacher=Teachers.query.filter_by(teacher_id=teacher_id).first()
        if teacher is None :
             return jsonify({"message": "The teacher with the id {} not found.".format(teacher_id)})
        else:
            data=request.json
            for key, value in data.items():
                setattr(teacher,key,value)
            db.session.commit()
            return ("The teacher has been updated successfuly"),200


class PartlyUpdateTeacher(Resource):
    def patch(self, teacher_id):
        teacher_id = int(teacher_id)
        teacher = Teachers.query.filter_by(teacher_id=teacher_id).first()
        if teacher is None:
            return jsonify({"message": "The teacher with the id {} not found.".format(teacher_id)})
        else:
            data = request.json
            for key, value in data.items():
                setattr(teacher, key, value)
            db.session.commit()
            return jsonify("The teacher has been successfully updated"), 200
        
class DeleteTeacher(Resource):
    def delete(self, teacher_id):
        teacher = Teachers.query.filter_by(teacher_id=int(teacher_id)).first()
        if teacher is None:
           return ({"message":"The teacher with the id {} does not exist".format(teacher_id)}),404
        #db.session.delete(teacher)
        db.session.commit()
        return ({"message":"The teacher with the id {} has been deleted".format(teacher_id)}),200
            