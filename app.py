from os import name
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from configs.base_config import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate

# import forms
from forms import LoginForm, SignUpForm, ScheduleForm

# create an instance of my app
app = Flask(__name__)

app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# creating an auth instance
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# import models
from models.user import User
from models.schedule import Schedule

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# @app.before_first_request
# def create_tables():
#     db.create_all()
#     # drop table 
#     # db.drop_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    # check for validation
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user:
            # check the password
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('schedules'))
        print('Invalid username or password')
        # return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/signup', methods =  ['GET', 'POST'])
def signup():

    form = SignUpForm()

    # get the data
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # hash the password
        hashed_password = generate_password_hash(password, method="sha256")

        new_user = User(first_name=first_name, last_name=last_name, 
                        username=username, email=email, password=hashed_password)

        # send the data to a db
        db.session.add(new_user)
        db.session.commit()
        print("User added successfully")
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)

@app.route('/schedules', methods = ['GET', 'POST'])
@login_required
def schedules():

    # fetch data
    schedules = Schedule.query.all()

    form = ScheduleForm()

    if form.validate_on_submit():
        working_hours = form.working_hours.data
        breaks = form.breaks.data
        break_activities = form.break_activities.data

        schedule = Schedule(working_hours=working_hours, breaks=breaks, break_activities=break_activities)

        # add data to db
        db.session.add(schedule)
        db.session.commit()
        print("Schedule created successfully")
        return redirect(url_for('schedules'))

    return render_template('my_schedule.html', form=form, name=current_user.username, schedules=schedules)

@app.route('/logout')
def logout(): 
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)