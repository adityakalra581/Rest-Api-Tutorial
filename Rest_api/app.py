from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
import os


# initialise the app
app=Flask(__name__)


## Setting up Database:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     

## Initialising the database:

db = SQLAlchemy(app)

## Initialise Marshmallow

ma = Marshmallow(app)

class Login(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name = db.Column(db.String(20), unique = True, nullable=False)
    email = db.Column(db.String(30), unique = True, nullable=False)
    phone = db.Column(db.String(10),unique=True, nullable=False)
    password = db.Column(db.String(10),nullable=False )
    
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

## Login Schema:
class LoginSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','phone','password')

## Initialising the Login Schema:

login_schema = LoginSchema()  
logins_schema = LoginSchema(many=True)  

# login_schema is for acquring single login information;
# logins_schema for multiple logins

## Add a login:
@app.route('/login',methods=['POST'])
def add_login():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    password = request.json['password']
    
    new_login = Login(name,email,phone,password)

    db.session.add(new_login)
    db.session.commit()

    return login_schema.jsonify(new_login)



## All logins
@app.route('/login',methods=['GET'])
def get_logins():
    all_logins = Login.query.all()
    result = logins_schema.dump(all_logins)
    return jsonify(result)


# For specific login query
@app.route('/login/<id>',methods=['GET'])
def get_login(id):
    login = Login.query.get(id)
    return login_schema.jsonify(login)





if __name__=="__main__":
    app.run(debug=True)