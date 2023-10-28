from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from sqlalchemy.exc import SQLAlchemyError
from flask_login import current_user, login_required
from flask_login import LoginManager, login_user, logout_user
from flask import request, jsonify

from flask.cli import with_appcontext, AppGroup

from App.models import Staff, Student, User,Review,ReviewList

from App.controllers import staff, student, addReview, get_staff_username,review,reviewlist

from.index import index_views

staff_view = Blueprint('staff_view', __name__, template_folder='../templates')



@staff_view.route('/signup',methods=['POST'])
def createStaff():
    data=request.get_json()
    taken_name=get_staff_username(data["username"])

    if(taken_name):
        return jsonify({"message": "Username already exists"}),401
    else: 
        user=staff.create_staff(data['username'],data['password']);
    if(user):
            return jsonify({"message": "Account Created"}),201
     
        

@staff_view.route('/login',methods=['GET'])
def login_action():
  data = request.get_json()
  staffs = Staff.query.filter_by(username=data['username']).first()

  if staffs and staffs.check_password(password=data['password']):  # check credentials

    flash('Logged in successfully.')  # send message to next page
    login_user(staffs)  # login the user
    return  jsonify({"message": "Login Sucesssful"}),201 # redirect to main page if login successful

  else:
    flash('Invalid username or password')  # send message to next page
    return jsonify({"message": "Incorrect Username or Password"}),401
  pass

@staff_view.route('/logout', methods=['GET'])
# @login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@staff_view.route('/addStudent', methods=['POST'])
# @login_required
def addStudent():
    data = request.get_json()
    taken_id = student.get_student(data['student_id'])

    if taken_id:
        return jsonify({"message": "Student already exists"}), 401
    else:
        new_student = student.create_student(data["student_id"], data["fname"], data["lname"])
        if new_student:
            return jsonify({"message": "Student added successfully"}), 201 
        else:
            return jsonify({"message":"Error Student already exists"})
    

@staff_view.route('/getstaffByUsername/<username>',methods=['GET'])
@login_required
def getStaffByUsername(username):
    return get_staff_username(username)


@staff_view.route('/createReview',methods=['POST'])
# @login_required
def createReview():

    data=request.get_json()
    new_review=review.create_review(data['student_id'],data['staff_id'],data['rating'],data['isPositive'],data['text'])
    
    if(new_review):
        return jsonify({"message": "Review Posted"}),201
    else:
        return jsonify({"message": "Error"}),401

@staff_view.route('/deleteReview',methods=['DELETE'])
# @login_required
def deleteReview():

    data=request.get_json()
    requested_review=Review.query.filter_by(id=data['reviewId']).first()

    if(requested_review):
            #find the review in reviewlist
            my_review=ReviewList.query.filter_by(review_id=data['reviewId']).first()
            my_review.delete()

            if(my_review):
                return jsonify({"message": "Your review has been deleted"}),200
            else:
                return jsonify({"message": "Error review does not exist"}),401
    else:
         return jsonify({"message": "Error review does not exist"}),401      

@staff_view.route('/searchStudent',methods=["GET"])
# @login_required
def searchStudent():
    data=request.get_json()
    requested_student=student.get_student(data["id"])
    if(requested_student):
        print(requested_student.get_json())
        return jsonify({"message": "Student Found", **requested_student.get_json()}),201
    else:
        return jsonify({"message": "Invalid Student Id Given"}),400


@staff_view.route('/getStudents', methods=['GET'])
def getStudentName():
    try:
        students_data = student.get_all_students_json()
        if students_data:
            return jsonify(students_data), 200
        else:
            return jsonify({"message": "No students found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500


@staff_view.route('/getReviews', methods=['GET'])
def getStudentReviews():
    data = request.get_json()

    requested_student=Student.query.filter_by(student_id=data["id"]).first()  # Use .get() to safely retrieve the student ID

    if requested_student:
            student_reviews = reviewlist.get_student_reviews(requested_student)#returns a json with all the reviews for a particular student
            
            return jsonify({"message": "Reviews Successfully retrieved", "reviews": student_reviews}), 200
    else:
        return jsonify({"message": "Invalid data sent. 'id' is missing or invalid"}), 400


@staff_view.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    
    requested_review=Review.query.filter_by(id=data['reviewId']).first()

    if(requested_review):
        
        if(data['vote']!=0):
            
            review_upvotes = staff.upVote(requested_review,data['vote'])
        else:
            review_upvotes= staff.downVote(requested_review,data['vote'])

        if(review_upvotes):
             return jsonify({"message": "Your vote has been recieved"}),200
        else:
            return jsonify({"message":"Error failed to log Vote"}),400
    else:
        return jsonify({"message":"Error failed to log Vote"}),400


@staff_view.route('/updateStudent', methods = ['PUT'])
def updateStudent():
    data = request.get_json()

    requested_student=Student.query.filter_by(id=data['studentId']).first()

    if(requested_student):
        requested_student.edit_name(data['fname'], data['lname'])
        return jsonify({"message": "Student updated"}),200
    else:
        return jsonify({"message": "Student does not exist"}),400



    
    

