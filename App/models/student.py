from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_id=db.Column(db.Integer,nullable=False)
    firstname=db.Column(db.String,nullable=False)
    lastname=db.Column(db.String,nullable=False)
    karma=db.Column(db.Integer, nullable=False)
    review = db.relationship('ReviewList', backref='student', lazy=True, cascade="all, delete-orphan")
    


    def __init__(self,student_id,firstname,lastname):
        self.student_id=student_id
        self.firstname=firstname
        self.lastname=lastname
        self.karma=0;

    def get_json(self):
        return{
            'id': self.id,
            'student Id':self.student_id,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'karma':self.karma
        }

    # def set_password(self, password):
    #     """Create hashed password."""
    #     self.password = generate_password_hash(password, method='sha256')
    
    # def check_password(self, password):
    #     """Check hashed password."""
    #     return check_password_hash(self.password, password)

