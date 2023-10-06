from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String,nullable=False)
    lastname=db.Column(db.String,nullable=False)
    karma=db.Column(db.Integer, nullable=fault,Default=1)
    review = db.relationship('Review', backref='student', lazy=True, cascade="all, delete-orphan")
    


    def __init__(self,id,firstname,lastname):
        self.id=id
        self.firstname=firstname
        self.lastname=lastname

    def get_json(self):
        return{
            'id': self.id,
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

