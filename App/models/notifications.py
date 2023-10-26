from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import Review
from App.models import Staff

class Notifications(db.Model, UserMixin):
    notificationID = db.Column(db.Integer, db.primary_key)
    text = db.Column(db.String(200),nullable=True) 
    staffID = db.Column(db.Integer, db.ForeignKey("staff.id"))

    
    def get_json(self):
        staff_name = Staff.get_staff(self.staff_id)
        return{
            'id': self.id,
            'notification': self.text,
            'Staff member':staff_name.username
        }