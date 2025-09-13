from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, ValidationError, EqualTo
from string import ascii_lowercase, ascii_uppercase, digits


class EditUsernameForm(FlaskForm):

    username = StringField("Edit you'r username", validators=[DataRequired(), length(min=2, max=30)])

    submit = SubmitField("Submit")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Enter Old password", validators=[DataRequired()])
    new_password = PasswordField(
        "Enter New password",
        validators=[DataRequired(), EqualTo('confirm_new_password', message="Passwords must match")]
    )
    confirm_new_password = PasswordField("Confirm New password", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_new_password(self, field):
        if field.data is None:
            return  # let DataRequired handle this

        errors = []

        if not any(c in ascii_uppercase for c in field.data):
            errors.append("Password must contain at least one uppercase letter")
        if not any(c in ascii_lowercase for c in field.data):
            errors.append("Password must contain at least one lowercase letter")
        if not any(c in digits for c in field.data):
            errors.append("Password must contain at least one digit")

        # Instead of raising list → extend field.errors
        if errors:
            for err in errors:
                field.errors.append(err)
            raise ValidationError("")  # raise dummy error so WTForms knows it failed




