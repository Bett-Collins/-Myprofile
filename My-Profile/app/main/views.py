from . import main
from flask import render_template


@main.route("/")
def index():
    
    message = 'Hello world'
    
    return render_template('index.html', message = message)