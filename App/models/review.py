from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class Review(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False) #set userid as a foreign key to user.id 
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False) #set userid as a foreign key to user.id 
    rating = db.Column(db.Integer,nullable=True)
    isPositive=db.Column(db.Boolean,nullable=False)#1 for if it is positive 0 if negative
    text = db.Column(db.String(200),nullable=True)



    def __init__(self,staff_id,studentID, rating,ispos, text):
        self.id=id
        self.staff_id=staff_id
        self.studentID = studentID
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

    def create_review(student_id, rating, comment):
        review = Review(student_id,rating,comment)
        db.session.add(review)
        db.session.commit()
        return


