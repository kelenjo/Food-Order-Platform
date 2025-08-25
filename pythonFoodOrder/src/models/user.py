from src.ext import db
from src.models import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, UserMixin):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    _password = db.Column(db.String)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password = generate_password_hash(password)

    def __repr__(self):
        return f"User name: {self.username}"

    def edit(self, form):
        self.username = form.username.data
        self.password = form.password.data
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

