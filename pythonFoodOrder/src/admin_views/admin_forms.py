from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email
from src.ext import db
from src.models import Role


class UserAdminForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password_plain = PasswordField("Password (leave blank to keep current)")
    roles = SelectMultipleField("Roles", coerce=int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.roles.choices = [(r.id, r.name) for r in db.session.query(Role).all()]
