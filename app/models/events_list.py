from app.models.event import *

event1= Event('20.11.2020','Party', 20, 'Edinburgh', 'Birthday Party', True) 
event2= Event('25.12.2020', 'Christmas', 34, 'Glasgow', 'Chrismas Dinner', False)
events_list = [event1, event2]

def add_new_event(event):
    events_list.append(event)