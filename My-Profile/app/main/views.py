from . import main
from flask import render_template
from flask_login import login_required

#....
@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
#....
    
    message = 'Hello world'
    
    return render_template('index.html', message = message)