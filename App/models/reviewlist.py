from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import Review,Student


class ReviewList(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    review_id=db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)
    student_id= db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)


    def __init__(self,student, review):
        self.review_id=review.id
        self.student_id = student.id
        


    def get_json(self):
        return{
            'Student id':self.student_id,
            'review':self.review_id
        }

    def delete(self):
    
            db.session.delete(self)
            db.session.commit()
            return True
        
#     def set_rating(self, rating):
#         self.rating = rating

#     def set_review(self, review):
#         self.review = review

#     def create_review(self, studid, rating, comment):
#         review = Review(studid,rating,comment)
#         db.session.add(review)
#         db.session.commit()
#         return


