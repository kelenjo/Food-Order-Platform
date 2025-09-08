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

    roles = db.relationship('Role', secondary="user_role", back_populates="users")

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

    @property
    def get_roles(self):
        return [user_role for user_role in self.roles]

    def has_role(self, role_name: str):
        for user_role in self.get_roles:
            if user_role.name == role_name:
                return True
        return False

    def get_role_names(self):
        return [user_role.name for user_role in self.get_roles]


class UserRole(BaseModel):

    __tablename__ = "user_role"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


class Role(BaseModel):

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    users = db.relationship('User', secondary="user_role", back_populates="roles")






