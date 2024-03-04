from models import db, Student, Class, Teachers, Fee

def seed_data():
    # Seed Students
    student1 = Student(student_name="John Doe", email="john@example.com", teacher_id=1)
    student2 = Student(student_name="Jane Smith", email="jane@example.com", teacher_id=2)

    # Seed Classes
    class1 = Class(course_title="Math", course_status="Active", teacher_id=1)
    class2 = Class(course_title="Science", course_status="Active", teacher_id=2)

    # Seed Teachers
    teacher1 = Teachers(teacher_name="Mr. Johnson", role="Math Teacher", class_id=1)
    teacher2 = Teachers(teacher_name="Ms. Anderson", role="Science Teacher", class_id=2)

    # Seed Fees
    fee1 = Fee(amount=10000.0, fee_status="Paid", student_id=1, class_id=1)
    fee2 = Fee(amount=150000.0, fee_status="Pending", student_id=2, class_id=2)

    # Add data to session and commit changes to the database
    db.session.add_all([student1, student2, class1, class2, teacher1, teacher2, fee1, fee2])
    db.session.commit()

    # Seed data into the database
    seed_data()
