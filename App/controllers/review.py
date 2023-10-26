from App.models import Review
from App.models import ReviewList,Student
from App.controllers import reviewlist,student
from App.database import db
from flask import jsonify

def create_review(student_id,staff_id,rating,isPositive,text):
    review = Review(staff_id,rating,isPositive,text)
    our_student=student.get_student(student_id)
    
    db.session.add(review)

    if(review):
        review_id=review.id
        reviewlist.add_review(review,our_student)
        db.session.commit()
        return review
    else:
            return None
    


def get_review_by_id(new_id):
    return Review.query.get(new_id)

def get_all_reviews(staff_id):#get all reviews for a specific staff
    reviews=Review.query.filter_by(staffId=staff_id).all()
    if not reviews:#if no reviews then return empty string
        return[]
    else:
        reviews_of= [review.get_json() for review in reviews]
        return jsonify(reviews_of)


# def get_all_users_json():
#     users = User.query.all()
#     if not users:
#         return []
#     users = [user.get_json() for user in users]
#     return users

# def update_review(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         return db.session.commit()
#     return None
    

