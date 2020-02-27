from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
import os


# initialise the app
app=Flask(__name__)


## Setting up Database:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False     ## Just for stop the warning

## Initialising the database:

db = SQLAlchemy(app)

## Initialise Marshmallow

ma = Marshmallow(app)

class Login(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name = db.Column(db.String(20), unique = True, nullable=False)
    email = db.Column(db.String(30), unique = True, nullable=False)
    phone = db.Column(db.String(10),unique=True, nullable=False)
    password = db .Column(db.String(10),nullable=False )
    
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

## Login Schema:
class LoginSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','password')

## Initialising the Login Schema:

login_schema = LoginSchema(strict=True)  
logins_schema = LoginSchema(many=True,strict=True)  

# login_schema is for acquring single login information;
# logins_schema for multiple logins




def get(self):
    pass

def post(self):
    pass



if __name__=="__main__":
    app.run(debug=True)