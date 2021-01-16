from sqlalchemy import Column, String, Integer, ForeignKey, Table
from flask_sqlalchemy import SQLAlchemy
import os

database_name = "online_education_system"
database_path = os.environ['DATABASE_URL']
#database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

student_courses = Table('student_courses', db.Model.metadata,
    Column('student_id', Integer, ForeignKey('student.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)
staff_courses = Table('staff_courses', db.Model.metadata,
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('staff_id', Integer, ForeignKey('staff.id'))
)

'''
Student

'''


class Student(db.Model):
    ___tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(120))
    address = Column(String(500))
    phone = Column(String(120))
    gender = Column(String(120))
    date_of_birth = Column(String(120))
    logincode = Column(String(120))
    specialization_id = Column(Integer, ForeignKey('specialization.id'), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=False)
    courses = db.relationship( "Courses", secondary=student_courses, back_populates="students")

    def __init__(self, name, email, address, phone, gender, date_of_birth, logincode, specialization_id, section_id):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.logincode = logincode
        self.specialization_id = specialization_id
        self.section_id = section_id

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth,
            'logincode': self.logincode,
            'specialization_id': self.specialization_id,
            'section_id': self.section_id
        }


'''
Staff

'''


class Staff(db.Model):
    ___tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(120))
    address = Column(String(500))
    phone = Column(String(120))
    gender = Column(String(120))
    job = Column(String(120))
    date_of_birth = Column(String(120))
    logincode = Column(String(120))
    data = db.relationship('Data', backref='staff', lazy='dynamic')
    courses = db.relationship( "Courses", secondary=staff_courses, back_populates="staff")

    def __init__(self, name, email, address, phone, gender, job, date_of_birth, logincode):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.gender = gender
        self.job = job
        self.date_of_birth = date_of_birth
        self.logincode = logincode

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'gender': self.gender,
            'job': self.job,
            'date_of_birth': self.date_of_birth,
            'logincode': self.logincode
        }


'''
Courses

'''


class Courses(db.Model):
    ___tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String(120))
    data = db.relationship('Data', backref='courses', lazy='dynamic')
    students = db.relationship("Student", secondary=student_courses, back_populates="courses")
    staff = db.relationship("Staff", secondary=staff_courses, back_populates="courses")

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }


'''
Section

'''


class Section(db.Model):
    ___tablename__ = 'section'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    Student = db.relationship('Student', backref='section', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }


'''
Specialization

'''


class Specialization(db.Model):
    ___tablename__ = 'specialization'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    student = db.relationship('Student', backref='specialization', lazy='dynamic')

    def __init__(self, name, code):
        self.name = name

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }


'''
Data 

'''


class Data(db.Model):
    ___tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    short_description = Column(String(120))
    description = Column(String)
    link = Column(String(500))
    type = Column(String(120))
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)

    def __init__(self, name, short_description, description, link, type, course_id, staff_id):
        self.name = name
        self.short_description = short_description
        self.description = description
        self.link = link
        self.type = type
        self.course_id = course_id
        self.staff_id = staff_id
        

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'short_description': self.short_description,
            'description': self.description,
            'link': self.link,
            'type': self.type,
            'course_id': self.course_id,
            'staff_id': self.staff_id
        }
