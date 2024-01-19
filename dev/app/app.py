from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'sqlite:///database.sqlite')

# initialize the database connection
database = SQLAlchemy(app)

# initialize database migration management
MIGRATE = Migrate(app, database)

from models import *

@app.route('/')
def view_guests():
    guests = Guest.query.all()
    return render_template('guest_list.html', guests=guests)


@app.route('/join', methods = ['GET'])
def view_registration_form():
    return render_template('guest_registration_form.html')


@app.route('/join', methods = ['POST'])
def join_guest():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    meal_option = request.form.get('meal_option')
    if not meal_option or meal_option == '':
        meal_option = "vegetarian"

    group_size = request.form.get('group_size')
    if not group_size or group_size=='':
        group_size = 1

    guest = Guest(first_name, last_name, email, group_size, meal_option)
    database.session.add(guest)
    database.session.commit()

    return render_template('guest_confirmation.html',
                           first_name=first_name, last_name=last_name, email=email, group_size=group_size, meal_option=meal_option)
