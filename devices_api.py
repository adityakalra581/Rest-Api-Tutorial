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
from datetime import datetime
from functools import wraps

# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand





app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

# admin = Admin(app)
# migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)
## Initialise Marshmallow

ma = Marshmallow(app)

## Specifically for Admin and creating new admin.





## MODEL 2: Devices

class Devices(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True)
    # transactions = db.relationship('Trasaction', backref = 'transactions')
    # fillups = db.relationship('Fiilup', backref = 'fillups')
    created = db.Column(db.DateTime, default = datetime.now())
    quantity_left = db.Column(db.Integer)
    # location = db.Column(db.String(100))
    tds = db.Column(db.Float(100))
    temp = db.Column(db.Float(100))

    def __init__(self, name):
        self.name = name
        # self.quantity_left = quantity_left
        # self.location = location
        # self.tds = tds
        # self.temp = temp

## Device Schema:
class DeviceSchema(ma.Schema):
    class Meta:
        fields = ('id','name','quantity_left','temp','tds','created')
## Initialising the Login Schema:
device_schema = DeviceSchema()  
devices_schema = DeviceSchema(many = True) 


## Add a Device:

@app.route('/device',methods=['POST'])
# @token_required
def add_device():
    
    name = request.json['name']
    # quantity_left = request.json['quantity_left']
    # location = request.json['location']
    # tds = request.json['tds']
    # temp = request.json['temp']
    
    new_device = Devices(name)

    db.session.add(new_device)
    db.session.commit()

    return device_schema.jsonify(new_device)



## All Devices

@app.route('/device/all',methods=['GET'])
# @token_required
def get_devices():
    
    all_devices = Devices.query.all()
    result = devices_schema.dump(all_devices)
    return jsonify(result)
    


## For specific device query

@app.route('/device/<id>',methods=['GET'])
# @token_required
def get_device(id):
    
    device = Devices.query.get(id)
    return device_schema.jsonify(device)


## Update a Device:

@app.route('/device/<id>',methods=['PUT'])
# @token_required
def update_device( id):
    
    device = Devices.query.get(id)
    name = request.json['name']
    temp = request.json['temp']
    quantity_left = request.json['quantity_left']
    tds = request.json['tds']
    
    device.name = name
    device.temp = temp
    device.quantity_left = quantity_left
    device.tds = tds

    db.session.commit()

    return device_schema.jsonify(device)

if __name__ == "__main__":
    app.run(debug=True)

