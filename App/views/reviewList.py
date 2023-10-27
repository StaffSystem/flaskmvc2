from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask.cli import with_appcontext, AppGroup

from App.models import Staff, Student, ReviewList

from.index import index_views

reviewList_view = Blueprint('reviewList_views', __name__, template_folder='../templates')



@reviewList_view.route('/reviews',methods=["GET"])
@login_required
def displayReviews():
    data = request.get_json()
    # student=Student.get_student(id)
    student = Student.get_student(id = data['id'])
    if(student):
        reviews=ReviewList.get_student_reviews(student.id)
    if(reviews):
        return jsonify({"message": "Reviews Displayed", **reviews.get_json()}),201
    else:
        return jsonify({"message": "No Reviews Found"}),404

