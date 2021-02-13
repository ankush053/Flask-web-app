from flask import Blueprint, render_template

devices = Blueprint('devices', __name__)

@devices.route('/devices', methods = ['GET', 'POST'])

def Device():

    return render_template('devices.html')

@devices.route('/devices/home', methods = ['GET', 'POST'])    
def home():

    return "this is home page"