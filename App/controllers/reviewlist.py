#review list is supposed to show a list of reviews for a specific student

from App.models import ReviewList
from App.models import Review
from App.models import Student
from App.controllers import student
from App.database import db


def add_review(review, student):
    rlist = ReviewList(review=review, student=student)
    db.session.add(rlist)
    db.session.commit()
    return rlist

def get_student_reviews(student):
    # Find review list entries for the given student
    review_list_entries = ReviewList.query.filter_by(student_id=student.id).all()

    student_reviews = []  # Initialize an empty list to store review JSON objects

    for entry in review_list_entries:
        review = Review.query.filter_by(id=entry.review_id).first()
        
        if review:  # Check if the review exists
            student_reviews.append(review.get_json())

    return student_reviews



# def get_user_by_username(username):
#     return User.query.filter_by(username=username).first()

# def get_user(id):
#     return User.query.get(id)

# def get_all_users():
#     return User.query.all()

# def get_all_users_json():
#     users = User.query.all()
#     if not users:
#         return []
#     users = [user.get_json() for user in users]
#     return users

# def update_user(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         return db.session.commit()
#     return None
    