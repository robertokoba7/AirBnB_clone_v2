#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """ Teardown """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ Function called with /states_list route """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('states_list.html',
                           Table="States",
                           states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
