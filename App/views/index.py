from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from sqlalchemy.exc import SQLAlchemyError
from App.models import db
from App.controllers import create_user
from App.controllers import staff, student

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

    #asd

@index_views.route("/getStaffs", methods=['GET'])
def getstaff():
    try:
        
        staffs=staff.get_all_staff()
        members = [staff.get_json() for staff in staffs]
        return jsonify(members)
    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500

        
    # return render_template('check.html', staffs=staffs)
    # else:
        # return jsonify({"Staff member not found"}),400
