from flask import Flask, request, abort, jsonify, render_template
from flask_cors import CORS
from sqlalchemy import select

from models import setup_db, Staff, Student, Courses, Data, student_courses, staff_courses, db

def create_app(test_config=None):
    # Create and configure the app 
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
    @app.route('/')
    def landing_page():
        return render_template('pages/index.html')

    @app.route('/login', methods=['POST'])
    def login():
        logincode = request.form.get('logincode', None)
        try:
            if logincode[0] == 'I' or logincode[0] == 'D' or logincode[0] == 'T':
                staff = Staff.query.filter(Staff.logincode == logincode).one()
                return render_template('pages/staff-profile.html',staff_data = {
                    'success': True,
                    'id': staff.id,
                    'name': staff.name,
                    'email': staff.email,
                    'address': staff.address,
                    'phone': staff.phone,
                    'gender': staff.gender,
                    'date_of_birth': staff.date_of_birth,
                    'job': staff.job,
                }),200
            elif logincode[0] == 'S':
                student = Student.query.filter(Student.logincode == logincode).one()
                return render_template('pages/student-profile.html',student_data ={
                    'success': True,
                    'id': student.id,
                    'name': student.name,
                    'email': student.email,
                    'address': student.address,
                    'phone': student.phone,
                    'gender': student.gender,
                    'date_of_birth': student.date_of_birth,
                }),200
            else:
                abort(401)
        except:
            abort(404)


    @app.route('/student/profile/<int:id>', methods=['GET'])
    def retrive_student(id):
        student = Student.query.get(id)
        if not student:
            abort(404)

        return render_template('pages/student-profile.html',student_data ={
                'success': True,
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'address': student.address,
                'phone': student.phone,
                'gender': student.gender,
                'date_of_birth': student.date_of_birth,
            }),200


    @app.route('/staff/profile/<int:id>', methods=['GET'])
    def retrive_staff(id):
        staff = Staff.query.get(id)
        if not staff:
            abort(404)

        return render_template('pages/staff-profile.html',staff_data = {
                    'success': True,
                    'id': staff.id,
                    'name': staff.name,
                    'email': staff.email,
                    'address': staff.address,
                    'phone': staff.phone,
                    'gender': staff.gender,
                    'date_of_birth': staff.date_of_birth,
                    'job': staff.job,
                }),200


    @app.route('/student/courses/<int:id>', methods=['GET'])
    def retrive_student_courses(id):
        courses = []
        try:
            course_id = db.session.execute(select([student_courses.c.course_id]).where(student_courses.c.student_id == id)).fetchall()
            for element in course_id:
                course = Courses.query.get(element[0])
                courses.append(course.format())
            return render_template('pages/student-courses.html',data = {
                    'id': id,
                    'success': True,
                    'courses_details': courses,
                    'length_of_courses': len(courses)
                }),200
        except:
            abort(404)


    @app.route('/staff/courses/<int:id>', methods=['GET'])
    def retrive_staff_courses(id):
        courses = []
        try:
            course_id = db.session.execute(select([staff_courses.c.course_id]).where(staff_courses.c.staff_id == id)).fetchall()
            for element in course_id:
                course = Courses.query.get(element[0])
                courses.append(course.format())
            return render_template('pages/staff-courses.html',data = {
                    'id': id,
                    'success': True,
                    'courses_details': courses,
                    'length_of_courses': len(courses)
                }),200
        except:
            abort(404)


    @app.route('/view/staff/course/<int:cid>/<int:id>', methods=['GET'])
    def retrive_staff_course_content(cid,id):
        try:
            selection = Data.query.filter(Data.course_id == cid).all()
            content = [result.format() for result in selection]
            course = Courses.query.get(cid).format()
            name = course['name']
            return render_template('pages/staff-course.html',data={
                    'id': id,
                    'name': name,
                    'success': True,
                    'course_content': content,
                    'length_of_content': len(content)
                }), 200
        except:
            abort(404)


    @app.route('/view/student/course/<int:cid>/<int:id>', methods=['GET'])
    def retrive_student_course_content(cid,id):
        try:
            selection = Data.query.filter(Data.course_id == cid).all()
            content = [result.format() for result in selection]
            course = Courses.query.get(cid).format()
            name = course['name']
            return render_template('pages/student-course.html',data={
                    'id': id,
                    'name': name,
                    'success': True,
                    'course_content': content,
                    'length_of_content': len(content)
                }), 200
        except:
            abort(404)


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404


    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        }), 401
                
            
            
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()


