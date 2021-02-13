from flask import Blueprint, render_template, jsonify
from frontend.controller.userController import userController
login = Blueprint('login', __name__)

@login.route('/login_page' , methods = ['GET', 'POST'])

def Login_page():

    return render_template('/login.html')

@login.route('/api/adduser', methods=['GET', 'POST'])
def adduser():
    data = {
            "userName": "ankush",
            "email": "ankush302@gmail.com",
            "password": "supersecret"
        }
    obj = userController()
    output = obj.addUser(data)
    return jsonify(output)
    