from flask import Flask
from models import db, Teachers, Student
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from student import student_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db.init_app(app)
#db == SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Hello World!'

app.register_blueprint(student_bp)

if __name__ == "__main__":
    app.run()
