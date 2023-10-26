from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import Staff


class Review(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False) #set userid as a foreign key to user.id 
    rating = db.Column(db.Integer,nullable=True)
    isPositive=db.Column(db.Boolean,nullable=False)#1 for if it is positive 0 if negative
    text = db.Column(db.String(200),nullable=True)
    # notifications = db.relationship('Notification', backref='notifications', lazy=True, cascade="all, delete-orphan")


    def __init__(self,staff_id, rating,ispos, text):
        self.staff_id=staff_id
        self.rating=1
        self.isPositive=ispos
        self.text=text
        


    def get_json(self):
        staff_name=Staff.get_staff(self.staff_id)

        return{
            'id': self.id,
            'Staff member':staff_name.username,
            'rating':self.rating,
            'review':self.text,
            'Positive':self.isPositive,

        }

    def set_rating(self, rating):
        self.rating = rating

    def set_review(self, review):
        self.text = review

    def create_review(self, staff_id,studentID, rating,ispos, text):
        review = Review(staff_id,studentID, rating,ispos, text)
        db.session.add(review)
        db.session.commit()
        return


