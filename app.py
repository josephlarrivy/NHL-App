from flask import Flask, render_template
app = Flask(__name__)
if __name__ == '__main__':
    app.run

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'woeifwofb3454rf'
debug = DebugToolbarExtension(app)

import requests



@app.route('/')
def home():
    """return homepage"""
    return render_template('home.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/players')
def homepage():
    return render_template('players.html')