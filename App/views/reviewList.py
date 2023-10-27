from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask.cli import with_appcontext, AppGroup

from App.models import Staff, Student, ReviewList

from.index import index_views

reviewList_views = Blueprint('reviewList_views', __name__, template_folder='../templates')



@reviewList_view.route('/reviews',methods=["GET"])
@login_required
def displayReviews():
    new_id = int(data['id'])
    student = Student.get_student(new_id)
    # student=Student.get_student(id)
    if(student):
        reviews=ReviewList.get_student_reviews(student.id)
        json_reviews = [review.get_json() for review in reviews]
    if(reviews):
        return jsonify({"message": "Reviews Displayed", **reviews_list}),201
    else:
        return jsonify({"message": "No Reviews Found"}),404

