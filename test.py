 
## This script will be used for Foreign Key testing and automatic model Update.

import flask
from flask import Flask,request, jsonify, make_response
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)


## Initialise Marshmallow

ma = Marshmallow(app)

## Specifically for Admin and creating new admin.

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String(50))
    owner_name = db.Column(db.Integer, db.ForeignKey('person.name'))
    # location = db.Column(Person)

#     def __init__(self, name, owner_name):
#         self.name = name
#         self.owner_name = owner_name

# ## Device Schema:
# class PetSchema(ma.Schema):
#     class Meta:
#         fields = ('id','name','owner_name')
# ## Initialising the Login Schema: 
# pets_schema = PetSchema(many = True)




class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True)
    pets = db.relationship('Pet', backref = 'owner')
    created = db.Column(db.DateTime, default = datetime.now())


#     def __init__(self, name):
#         self.name = name

# ## Device Schema:
# class PersonSchema(ma.Schema):
#     class Meta:
#         fields = ('id','name','created')
# ## Initialising the Login Schema: 
# person_schema = PersonSchema(many = True)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/person',methods=['GET','POST'])
def person():
    if request.method == 'POST':

        data = request.get_json()
        new_person = Person(name=data['name'])

        db.session.add(new_person)
        db.session.commit()

        return jsonify({'message' : 'New Person Added!'})
    else:
        
        all_person = Person.query.all()
        output = []
        for p in all_person:
            p_data = {}
            p_data['id'] = p.id
            p_data['name'] = p.name
            # p_data['pets'] = p.pets
            p_data['created']= p.created
            output.append(p_data)
        return jsonify({'person': output})

@app.route('/pets',methods=['GET','POST'])
def pets():
    
    if request.method == "POST":

        data = request.get_json()
        new_pet = Pet(name=data['name'], 
                        owner_name=data['owner_name'])
        # name = request.json['name']
        # owner_name = request.json['owner_name']

        # new_pet = Pet(name,owner_name)

        db.session.add(new_pet)
        db.session.commit()

        return jsonify({'message' : 'New Pet Added!'})

    else:
        all_pets = Pet.query.all()
        output = []
        for p in all_pets:
            p_data = {}
            p_data['id'] = p.id
            p_data['name'] = p.name
            p_data['owner_name'] = p.owner_name
            output.append(p_data)
        return jsonify({'Pets': output})


## So if we want to find the Person with their pets:

## Query: db.session.query(Person, Pet).outerjoin(Pet, Person.name == Pet.owner_name).all()

@app.route('/person/pet',methods = ['GET'])
def join_pets_person():
        r = db.session.query(Person.name, Pet.name).outerjoin(Pet, Person.name == Pet.owner_name).all()
        result = str(r)
        return result
        # x = {}
        # for result in r:
            # if result[1]:
                # x.setdefault("name",[]).append(result[0])       
                #  print('Owner: {}, Pet:{}'.format(result[0].name,result[1].name))
                
@app.route('/person/pet/<name>')
def pets_analysis(name):
    r = db.session.query(Person.name, Pet.name).outerjoin(Pet, Person.name == Pet.owner_name).all()
    result = []
    for i in r:
        if i[0] == name:
            result.append(i[1])
    return str(result)
            




if __name__ == "__main__":
    # db.create_all()
    # manager.run()
    app.run(debug = True)
