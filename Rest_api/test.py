from flask import Flask
from flask_restful import Resource, Api

app= Flask(__name__)
api=Api(app)


data=[]

class Hello(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            "Hello":"World"
        }

class Person(Resource):
    def get(self,name):
        for x in data:
            if x['data'] == name:
                return x
        return {'data':None}


    def post(self,name):
        temp={'data':name}
        data.append(temp)
        return temp


    def delete(self,name):
        for i,x in enumerate(data):
            if x['data'] == name:
                temp = data.pop(i)
                return {'Node':'Deleted'}



api.add_resource(Person,'/Name/<string:name>')
#api.add_resource(Hello,'/')
if __name__=='__main__':
    app.run(debug=True)