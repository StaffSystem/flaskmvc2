from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class Review(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False) #set userid as a foreign key to user.id 
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False) #set userid as a foreign key to user.id 
    rating = db.Column(db.Integer,nullable=True)
    isPositive=db.Column(db.Boolean,nullable=False)#1 for if it is positive 0 if negative
    review = db.Column(db.String(200),nullable=True)



    def __init__(self,studentID, rating, review):
        self.studentID = studentID
        self.rating=rating
        self.review=review


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


