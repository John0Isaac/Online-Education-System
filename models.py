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
    national_id = Column(String)
    date_of_birth = Column(String)
    logincode = Column(String)
    specialization_id = Column(Integer, ForeignKey('specialization.id'), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=False)

    def __init__(self, name, email, address, phone, gender, national_id, date_of_birth, logincode, specialization_id, section_id):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.gender = gender
        self.national_id = national_id
        self.date_of_birth = date_of_birth
        self.logincode = logincode
        self.specialization_id = specialization_id
        self.section_id = section_id

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
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'gender': self.gender,
            'national_id': self.national_id,
            'date_of_birth': self.date_of_birth,
            'logincode': self.logincode,
            'specialization_id': self.specialization_id,
            'section_id': self.section_id
        }