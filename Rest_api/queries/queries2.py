## TEST SCRIPT:
## Version 3.0

## TASKS:

## 1. Creating a subquery in SQLAlchemy which will give the frequency of deliveries on specific dates in Desc order.
## 2. Converting GPS cordinates into location and store it in db.
## 3. Migrating Database.
## 4. Creating a subquery in SQLAlchemy which will give the answer of "Which locations deliveries are generally high"

## IMPORTS:

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
from datetime import date
from functools import wraps

from flask_cors import CORS

from sqlalchemy import func, distinct, desc

## For cordinates to location.
import geopy
from geopy import Nominatim

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# ***************************************************************


## os.environ.get('SECRET_KEY')
##  os.environ.get('DATABASE_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = "2ewfn23r2hroejfi2fi2h4fh4e2h24hroi"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

# *******************************************************************


## MODEL 3: Deliveries [Keeping driver's email as foreign key.]

class Deliveries(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    driver_name = db.Column(db.String(30))
    driver_email = db.Column(db.String(50))
    amount = db.Column(db.Integer)
    temp = db.Column(db.Float(10))
    location = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(100))
    locality = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default = datetime.datetime.now())
    date = db.Column(db.String(50), default = datetime.date.today().strftime("%d/%m/%Y"))
    time = db.Column(db.String(50), default = datetime.datetime.now().time().strftime("%H:%M:%S"))
    day = db.Column(db.String(50), default = datetime.datetime.now().strftime("%A"))

# now = datetime.datetime.now()
# print(now.strftime("%A"))

# import datetime
# from datetime import date

# d = date.today()
# t = datetime.datetime.now().time()

# print(d)
# print(type(d))
# print(t)
# print(type(t))


# print(datetime.date.today())


## ROUTES:

## Route 11 : /delivery/create
## Creating a delivery.



@app.route('/delivery/create', methods=['POST'])
def create_delivery():

    data = request.get_json()
    try:
        new_del = Deliveries(driver_name=data['driver_name'], driver_email=data['driver_email'], amount=data['amount'], 
                            temp=data['temp'], location=data['location'],date=data['date'],
                            city=((Nominatim(user_agent='test/1').reverse(data['location']).raw)['address']['city']), 
                            address=(Nominatim(user_agent='test/1').reverse(data['location']).address), 
                            locality=((Nominatim(user_agent='test/1').reverse(data['location']).raw)['address']['county']))
    except:
        new_del = Deliveries(driver_name=data['driver_name'], driver_email=data['driver_email'], amount=data['amount'], 
                            temp=data['temp'], location=data['location'],date=data['date'],
                            city=((Nominatim(user_agent='test/1').reverse(data['location']).raw)['address']['state']), 
                            address=(Nominatim(user_agent='test/1').reverse(data['location']).address), 
                            locality=((Nominatim(user_agent='test/1').reverse(data['location']).raw)['address']['county']))

    db.session.add(new_del)
    db.session.commit()
    return jsonify({'message' : 'New Delivery created!'})


## Get all deliveries.
## Route 12 : /delivery/all

@app.route('/delivery/all', methods=['GET'])
# @token_required
def get_deliveries():
# def get_all_deliveries():
    # if not current_user.admin:
    #     return jsonify({'message' : 'User is not an authorized Admin!, Only Admin can access these records.'})

    deliveries = Deliveries.query.all()
    output = []
    for i in deliveries:
        del_data = {}
        del_data['id'] = i.id
        del_data['driver_name'] = i.driver_name
        del_data['driver_email'] = i.driver_email
        del_data['amount'] = i.amount
        del_data['temp'] = i.temp
        del_data['location'] = i.location
        del_data['city'] = i.city
        del_data['locality'] = i.locality
        del_data['address'] = i.address
        del_data['timestamp'] = i.timestamp
        del_data['date'] = i.date
        del_data['time'] = i.time
        del_data['day'] = i.day
        output.append(del_data)

    return jsonify({'deliveries' : output})


# *************************************************

## Question: On which days deliveries were highest”

## Query: SELECT date, COUNT(date) AS Frequency FROM Deliveries GROUP BY date ORDER BY COUNT(date) DESC

##  db.session.query(Table.column, func.count(Table.column)).group_by(Table.column).all()


@app.route('/delivery/date', methods=['GET'])
def date_del():
    date = db.session.query(Deliveries.date, func.count(Deliveries.date), Deliveries.day).group_by(Deliveries.date, Deliveries.day).order_by(func.count(Deliveries.date).desc()).all()
    return str(date)



## Query: Which locations deliveries are generally high.
## 1. Using area: It is the first value in address.
## 2. Using Locality: County in address.


# @app.route('/delivery/area', methods=['GET'])
# def area_del():
#     area = db.session.query(Deliveries.area, func.count(Deliveries.area), Deliveries.address).group_by(Deliveries.area).order_by(func.count(Deliveries.area).desc()).all()
#     return str(area)


@app.route('/delivery/locality', methods=['GET'])
def locality_del():
    location = db.session.query(Deliveries.locality, func.count(Deliveries.locality), Deliveries.city).group_by(Deliveries.locality, , Deliveries.city).order_by(func.count(Deliveries.locality).desc()).all()
    return str(location)


if __name__ == "__main__":
    app.run(debug=True)
    # manager.run()