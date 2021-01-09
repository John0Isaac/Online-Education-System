from operator import add
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import psycopg2

database_name = "online_education_system"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

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


'''
Student

'''


class Student(db.Model):
    ___tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(120))
    address = Column(String)
    phone = Column(String(120))
    gender = Column(String)
    date_of_birth = Column(String)
    logincode = Column(String)
    specialization_id = Column(Integer, ForeignKey('specialization.id'), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=False)

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
    address = Column(String)
    phone = Column(String(120))
    gender = Column(String)
    job = Column(String)
    date_of_birth = Column(String)
    logincode = Column(String)
    data_id = Column(Integer, ForeignKey('data.id'), nullable=False)

    def __init__(self, name, email, address, phone, gender, job, date_of_birth, logincode, data_id):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.gender = gender
        self.job = job
        self.date_of_birth = date_of_birth
        self.logincode = logincode
        self.data_id = data_id

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
            'logincode': self.logincode,
            'data': self.data_id
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
    number = Column(String)
    Student = db.relationship('Student', backref='section', lazy='dynamic')

    def __init__(self, number):
        self.number = number

    def format(self):
        return {
            'id': self.id,
            'number': self.name
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
    link = Column(String(120))
    type = Column(String)
    comment = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    def __init__(self, name, short_description, description, link, type, comment, course_id):
        self.name = name
        self.short_description = short_description
        self.description = description
        self.link = link
        self.type = type
        self.comment = comment
        self.course_id = course_id
        staff = db.relationship('Staff', backref='data', lazy='dynamic')

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
            'comment': self.comment,
            'course_id': self.course_id
        }
