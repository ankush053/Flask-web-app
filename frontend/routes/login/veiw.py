from flask import Blueprint, render_template

login = Blueprint('login', __name__)

@login.route('/login_page' , methods = ['GET', 'POST'])

def Login_page():

    return render_template('/login.html')