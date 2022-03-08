from . import main
from flask import render_template
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import Reviews, User
#....

#.....
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#.....
@main.route('/')
@login_required
def new_review(id):
#....
    
    message = 'Hello world'
    
    return render_template('index.html', message = message)