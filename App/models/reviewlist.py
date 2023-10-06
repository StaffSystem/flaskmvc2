from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class ReviewList(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    review_id=db.Column(db.Integer, db.ForeignKey('Review.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('Student.id'), nullable=False)


    def __init__(self,studentID, review_id):
        self.student_id = studentID
        self.review_id=review_id


    def get_json(self):
        return{
            'id': self.id,
            'rating':self.rating,
            'review':self.review
        }

    def set_rating(self, rating):
        self.rating = rating

    def set_review(self, review):
        self.review = review

    def create_review(studid, rating, comment):
        review = Review(studid,rating,comment)
        db.session.add(review)
        db.session.commit()
        return


