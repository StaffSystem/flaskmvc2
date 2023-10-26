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
    get_all_staff,
    get_staff,
    get_staff_username
)

app = create_app()
migrate = get_migrate(app)

LOGGER = logging.getLogger(__name__)

staff_test=AppGroup("staff",help='Tests Staff functions')

class StaffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        staff=Staff("bob","bobpass")
        assert staff.usernamw=="bob"

    def test_get_json(self):
        staff=Staff("bob","bobpass")
        staff_json=staff.get_json
        self.assertDictEqual(staff_json,"id":None,"username":"bob")


@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert login("bob", "bobpass") != None

class StaffIntergrationTests(unittest.TestCase):

    def create_staff_test(self):
        user = create_staff(username="bob2",password="bob2pass")
        assert user.username == "bob"
#commit

    def update_staff_username_test(self):
        staff=get_staff(1)
        if staff:
            staff.username="bill"
            db.session.add(staff)
            db.session.commit()
        assert staff.username=="bill"


    def test_get_staff_username(self):
        staff=create_staff("bob","bobpass")
        staffid=get_staff_username(username="bob")
        if staffid:
            print (staff)
            assert staff.username=="bob"
        print ("staff not found")

    def test_get_all_staff(self):
        staff_json = get_all_staff()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], staff_json)