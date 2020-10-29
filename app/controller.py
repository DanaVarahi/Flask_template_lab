from flask import render_template, request
from app import app
from app.models.events_list import *
from app.models.event import *

@app.route('/')
def index():
   return render_template('index.html', title='Home', my_events=events_list)

@app.route('/add-event', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_no_of_guests = request.form['no_of_guests']
    event_location = request.form['location']
    event_description = request.form['description']
    event_recurring = True if 'recurring' in request.form else False
    new_event = Event( event_date, event_name, event_no_of_guests, event_location, event_description, event_recurring )
    add_new_event(new_event)
    return render_template('index.html', title='Home', my_events=events_list)