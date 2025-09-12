from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, length, ValidationError
from string import ascii_lowercase, ascii_uppercase, digits


class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired(), length(min=2, max=30)])
    email = EmailField("Enter email", validators=[DataRequired()])
    password = PasswordField("Enter password", validators=[DataRequired()])

    submit = SubmitField("Register")

    def validate_password(self, field):
        contains_upcase = False
        contains_lowcase = False
        contains_digits = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_upcase=True
            if char in ascii_lowercase:
                contains_lowcase=True
            if char in digits:
                contains_digits=True

        if contains_upcase == False:
            raise ValidationError("Password must contain UpperCase Letter")
        if contains_lowcase == False:
            raise ValidationError("Password must contain LowerCase Letter")
        if contains_digits == False:
            raise ValidationError("Password must contain Digits Letter")


class LoginForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired()])

    submit = SubmitField("Log in")


