from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import Review
