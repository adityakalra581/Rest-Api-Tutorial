## TASK: To generate a jwt token on succesful login using Basic Auth with email and hashed password.




import flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import Flask,request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
import os
import uuid                                                                   ## For generating random public id.
from werkzeug.security import generate_password_hash, check_password_hash     ## for password hashing
import jwt                                                                    ## jason web token
import datetime
from functools import wraps

# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand





app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    driver_id = db.Column(db.String(8), unique=True)
    driver_name = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)  
    password = db.Column(db.String(80))
    reg_num = db.Column(db.String(10))
    aadhar_num = db.Column(db.String(16))
    # deliveries = db.relationship('Trasaction', backref = 'dekiveries')
    created = db.Column(db.DateTime, default = datetime.datetime.now())




@app.route('/driver/create',methods=['POST'])
# @token_required
def create_driver():
    

    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_driver = Driver(driver_id=str(uuid.uuid4()), email=data['email'], password=hashed_password)
    db.session.add(new_driver)
    db.session.commit()
    return jsonify({'message' : 'New driver created!'})

## Route 6: Get All Driver

@app.route('/driver/all',methods=['GET'])
# @token_required
# def get_all_users(current_user):
def get_devices():
    # if not current_user.admin:
    #     return jsonify({'message' : 'Cannot perform that function!'})

# 'id','driver_name','email','password','reg_num','aadhar_num','created'

    driver = Driver.query.all()
    output = []
    for d in driver:
        driver_data = {}
        driver_data['id'] = d.id
        driver_data['driver_id'] = d.driver_id
        driver_data['driver_name'] = d.driver_name
        driver_data['password'] = d.password
        driver_data['email'] = d.email
        driver_data['reg_num'] = d.reg_num
        driver_data['aadhar_num'] = d.aadhar_num
        driver_data['created'] = d.created
        output.append(driver_data)

    return jsonify({'driver' : output})


## NOTE: auth only has username and email attributes. You can use email, name or anything as username.
## I have used email for authentication as driver table has unique email.
## Just replace email instead of the parameter you wanna use.  

@app.route('/driver/login')
def driver_login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    driver = Driver.query.filter_by(email=auth.username).first()

    if not driver:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(driver.password, auth.password):
        token = jwt.encode({'driver_id' : driver.driver_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


if __name__ == "__main__":
    app.run(debug=True)