from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask.cli import with_appcontext, AppGroup

from App.models import Staff, Student, ReviewList

from.index import index_views

reviewList_view = Blueprint('reviewList_views', __name__, template_folder='../templates')



@reviewList_view.route('/reviews',method=["GET"])
@login_required
def displayReviews(id):
    student=Student.get_student(id);
    if(student):
        reviews=ReviewList.get_student_reviews(student.id)
    if not reviews:#if no reviews then return empty string
        return[]
    else:
        return reviews

