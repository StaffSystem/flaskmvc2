import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from App.controllers.user import create_user

from App.main import create_app
from App.database import db, create_db, get_migrate
from App.models import User

import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup


from App.controllers.staff import(
    Staff,
    create_staff,
    get_staff,
    get_staff_username
)

app = create_app()
migrate = get_migrate(app)

LOGGER = logging.getLogger(__name__)

staff_test=AppGroup("staff",help='Tests Staff functions')


class StaffUnitTests(unittest.TestCase):
    @staff_test.command("create_Staff", help='Test create Staff function')
    @click.argument("username", default="rob")
    @click.argument("password", default="robpass")
    def create_staff_test(self,username,password):
        user = Staff(username, password)
        assert user.username == "rob"
#commit

    def update_staff_username_test(self,new_id,username):
        staff=get_staff(new_id)
        if staff:
            staff.username=username
            db.session.add(staff)
            db.session.commit()
        assert staff.username=="bill"



    @staff_test.command("get_staff_name", help='Test get Staff function')
    def test_get_staff_id(self):
        staff=create_staff("bob","bobpass")
        staffid=get_staff_username(username="bob")
        if staffid:
            print (staff)
        print ("staff not found")

app.cli.add_command(staff_test)