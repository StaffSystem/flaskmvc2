#review list is supposed to show a list of reviews for a specific student

from App.models import ReviewList
from App.models import Review
from App.controllers import student
from App.database import db


def add_review(review,student):
    rlist = ReviewList(review,student)
    db.session.add(rlist)
    db.session.commit()
    return rlist

def get_student_reviews(student_id):
    reviews=Review.query.filter_by(student_id=student_id).all()
    if not reviews:#if no reviews then return empty string
        return[]
    reviews_of= [review.get_json() for review in reviews]
    return reviews_of


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
    