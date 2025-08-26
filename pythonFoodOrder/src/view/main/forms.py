from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Email, Optional


class FeedbackForm(FlaskForm):
    rating = RadioField('Rating', choices=[('5','5'),('4','4'),('3','3'),('2','2'),('1','1')], validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
