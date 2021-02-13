from flask import Blueprint,render_template

api = Blueprint('api', __name__)

@api.route('/api', methods = ['GET', 'POST'])

def Api():
    
    return render_template('/api.html')
    