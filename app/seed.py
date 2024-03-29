from app import app, db
from models import Student, Class, Teachers, Fee

def seed_data():
    with app.app_context():
        # Create some students
        student1 = Student(student_name='John Doe', email='john@example.com')
        student2 = Student(student_name='Jane Smith', email='jane@example.com')
        student3 = Student(student_name='Alice Johnson', email='alice@example.com')

        # Create some teachers
        teacher1 = Teachers(teacher_name='Mr. Smith', role='Math Teacher')
        teacher2 = Teachers(teacher_name='Mrs. Johnson', role='English Teacher')

        # Add students and teachers to the session
        db.session.add_all([student1, student2, student3, teacher1, teacher2])
        db.session.commit()

        # Create some classes
        class1 = Class(course_title='Mathematics', course_status='Active', teacher=teacher1)
        class2 = Class(course_title='English Literature', course_status='Active', teacher=teacher2)
        class3 = Class(course_title='Science', course_status='Active', teacher=teacher1)

        # Assign students to classes
        class1.students.append(student1)
        class2.students.append(student2)
        class3.students.append(student3)

        # Add classes to the session
        db.session.add_all([class1, class2, class3])
        db.session.commit()

        # Create some fees
        fee1 = Fee(amount=100.0, fee_status='Paid', student_id=student1.student_id)
        fee2 = Fee(amount=150.0, fee_status='Unpaid', student_id=student2.student_id)
        fee3 = Fee(amount=120.0, fee_status='Paid', student_id=student3.student_id)

        # Add fees to the session
        db.session.add_all([fee1, fee2, fee3])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
