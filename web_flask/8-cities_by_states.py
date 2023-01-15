#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy session
    """
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """
    Displays the html page of cities with states
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    s_c = []
    for state in states:
         s_c.append([state, sorted(state.cities, key=lambda x: x.name)])
    return render_template('8-cities_by_states.html', states=s_c, h="States")

if __name__ == '__main__':
    """
    Runs when this script is not imported
    """
    app.run(host="0.0.0.0", port=5000)
