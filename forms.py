from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Email, Length

# login form
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remmber me')

# sign up form
class SignUpForm(FlaskForm):
    first_name = StringField('first name', validators=[InputRequired(), Length(min=4, max=15)])
    last_name = StringField('last name', validators=[InputRequired(), Length(min=4, max=15)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

#  schedule form
class ScheduleForm(FlaskForm):
    working_hours = IntegerField('working hours', validators=[InputRequired()])
    breaks = IntegerField('breaks', validators=[InputRequired()])
    break_activities = StringField('break_activities', widget=TextArea(), validators=[InputRequired(), Length(min=4, max=255)])