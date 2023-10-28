# from flask import Blueprint, request
from App.models import Staff
from App.models import Review
from App.models import User
from App.models import Student,ReviewList
from App.database import db
from App.controllers import create_review
from flask import jsonify

# staff_view = Blueprint('staff_views', __name__, template_folder='../templates')

def create_staff(username,password):
    newStaff=Staff(username,password)
    db.session.add(newStaff)
    db.session.commit()
    return newStaff

def get_staff(new_id):
    staff=Staff.query.get(new_id)
    if (staff):
        return staff
    return None

def get_all_staff():
    staffs = Staff.query.all()
    if (staffs):
        return staffs
    return None

def get_staff_username(username):
    staff=Staff.query.filter_by(username=username).first()
    if (staff):
        return staff
    return None

def update_staff_username(new_id,username):
    staff=get_staff(new_id)
    if (staff):
        staff.username=username
        db.session.add(staff)
        return db.session.commit()
    return None

def update_staff_password_(new_id,password):
    staff=get_staff(new_id)
    if staff:
        staff.password=password
        db.session.add(staff)
        return db.session.commit()
    return None

def search_student(studid):
    return User.get_user(studid)


def search_student_by_name(username):
    return User.get_user_by_username(username)

def upVote(review,vote):
    #in this case we pass the review instance itself (just like with self)
    review.rating+=1
    reviewListpos= ReviewList.query.filter_by(review_id=review.id).first()
    our_student=Student.query.filter_by(id=reviewListpos.student_id).first()

    our_student.edit_karma(vote)
    review.set_rating(review.rating)
    return review #idk why returning review does not work here
    
def downVote(review,vote):
    review.rating-=1
    reviewListpos=ReviewList.query.filter_by(review_id=review.id).first()
    our_student=Student.query.filter_by(id=reviewListpos.student_id).first()
    our_student.edit_karma(vote)
    review.set_rating(review.rating)
    return review #idk why returning review does not work here
    
    
def addReview(data):
    review=create_review(data['studentID'],data["Staffid"],data['rating'],data['isPositive'],data['text'])
    return review
    


