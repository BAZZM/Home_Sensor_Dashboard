from datetime import datetime
from website import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    dob = db.Column(db.String(20))
    ecname = db.Column(db.String(64))
    ecphone = db.Column(db.String(20))
    ecemail = db.Column(db.String(120))
    multi = db.Column(db.Boolean, default=False, server_default="false")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer)

class Flags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    propertyID = db.Column(db.Integer)
    userID = db.Column(db.Integer)
    datetime = db.Column(db.String(20))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()