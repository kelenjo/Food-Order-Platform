from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, ValidationError
from string import ascii_lowercase, ascii_uppercase, digits


class EditUsernameForm(FlaskForm):

    username = StringField("Edit you'r username", validators=[DataRequired(), length(min=2, max=30)])

    submit = SubmitField("Submit")


class ChangePasswordForm(FlaskForm):

    current_password = PasswordField("Enter Old password")
    new_password = PasswordField("Enter New password", validators=[DataRequired()])
    confirm_new_password = PasswordField("Enter New password", validators=[DataRequired()])

    submit = SubmitField("Submit")

    def validate_new_password(self, field):
        contains_upcase = False
        contains_lowcase = False
        contains_digits = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_upcase = True
            if char in ascii_lowercase:
                contains_lowcase = True
            if char in digits:
                contains_digits = True

        if contains_upcase == False:
            raise ValidationError("Password must contain UpperCase Letter")
        if contains_lowcase == False:
            raise ValidationError("Password must contain LowerCase Letter")
        if contains_digits == False:
            raise ValidationError("Password must contain Digits Letter")

