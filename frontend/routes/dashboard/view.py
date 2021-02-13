from flask import Blueprint,render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods = ['GET', 'POST'])

def Dashboard():

    return render_template('/dashboard.html')
    