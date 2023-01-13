#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello():
    """
    Returns the states to the client
    """
    states = storage.all(State)
    sorted_states = sorted(states.items(), key=lambda x: x[1].name)
    for index, value in enumerate(sorted_states):
        state_id = value[0].split('.')[1]
        state = (state_id, value[1])
        sorted_states[index] = state
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy session
    """
    storage.close()

if __name__ == '__main__':
    """
    Runs when this script is not imported
    """
    app.run(host="0.0.0.0", port=5000)
