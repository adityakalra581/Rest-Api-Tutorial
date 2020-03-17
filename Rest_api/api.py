from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid                                                                   ## For generating random public id.
from werkzeug.security import generate_password_hash, check_password_hash     ## for password hashing
import jwt                                                                    ## jason web token
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True,nullable=False)
    source = db.Column(db.String(50))
    status = db.Column(db.Boolean)
    

class Transactions(db.Model):
    trans_id = db.Column(db.Integer, primary_key=True,nullable=False)
    order_id = db.Column(db.Integer)
    status = db.Column(db.Boolean)

def token_required(f):
    @wraps(f)
    ## args : Positional argument
    ## kwargs : Keyword Arguments
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users' : output})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user' : user_data})

@app.route('/user', methods=['POST'])
## For creating a user only POST is required.
#@token_required
def create_user():
    # if not current_user.admin:
    #     return jsonify({'message' : 'Cannot perform that function!'})

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')
    # https://en.bitcoinwiki.org/wiki/SHA-256
    ## Simply put : SHA-256 is a member of the SHA-2 cryptographic hash functions designed by the NSA. SHA stands for Secure Hash Algorithm.

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'New user created!'})

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user.admin = True
    db.session.commit()

    return jsonify({'message' : 'The user has been promoted!'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message' : 'The user has been deleted!'})

@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

@app.route('/order', methods=['GET'])
@token_required
def get_all_orders(current_user):
    orders = Orders.query.all()

    output = []

    for order in orders:
        order_data = {}
        order_data['order_id'] = order.order_id
        order_data['source'] = order.source
        order_data['status'] = order.status
        output.append(order_data)

    return jsonify({'orders' : output})

@app.route('/order/<order_id>', methods=['GET'])
@token_required
def get_one_order(current_user, order_id):
    order = Orders.query.filter_by(order_id=order_id).first()

    if not order:
        return jsonify({'message' : 'No order found!'})

    order_data = {}
    order_data['order_id'] = order.order_id
    order_data['source'] = order.source
    order_data['status'] = order.status

    return jsonify(order_data)

@app.route('/order', methods=['POST'])
@token_required
def create_order(current_user):
    data = request.get_json()

    new_order = Orders(source=data['source'], status=False)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message' : "Order created!"})

@app.route('/order/<order_id>', methods=['DELETE'])
@token_required
def delete_order(current_user, order_id):
    order = Orders.query.filter_by(order_id=order_id,).first()

    if not order:
        return jsonify({'message' : 'No order found!'})

    db.session.delete(order)
    db.session.commit()

    return jsonify({'message' : 'order deleted!'})


## For Transactions:

@app.route('/transaction', methods=['GET'])
@token_required
def get_all_transactions(current_user):
    trans = Transactions.query.all()

    if not trans:
        return jsonify({'message':'No Transaction Found'})


    output = []

    for tran in trans:
        tran_data = {}
        tran_data['trans_id'] = tran.trans_id
        tran_data['order_id'] = tran.order_id
        tran_data['status'] = tran.status
        output.append(tran_data)

    return jsonify({'trans' : output})

@app.route('/transaction/<trans_id>', methods=['GET'])
@token_required
def get_one_trans(current_user, trans_id):
    trans = Transactions.query.filter_by(trans_id=trans_id).first()

    if not trans:
        return jsonify({'message' : 'No transaction found!'})

    tran_data = {}
    tran_data['trans_id'] = tran.trans_id
    tran_data['source'] = tran.order_id
    tran_data['status'] = tran.status

    return jsonify(tran_data)

@app.route('/transactions', methods=['POST'])
# @token_required
def create_trans():
    data = request.get_json()

    new_trans = Transactions(order_id=data['order_id'], status=False)
    db.session.add(new_trans)
    db.session.commit()

    return jsonify({'message' : "Transaction created!"})


@app.route('/transaction/<trans_id>', methods=['DELETE'])
@token_required
def delete_trans(current_user, trans_id):
    trans = Transactions.query.filter_by(trans_id=trans_id,).first()

    if not trans:
        return jsonify({'message' : 'No Transaction found!'})

    db.session.delete(trans)
    db.session.commit()

    return jsonify({'message' : 'Transcation deleted!'})




if __name__ == '__main__':
    app.run(debug=True)


"""
@app.route.('/transacation/<orders>=<t.status>)
def add_transactions():

    transactions.status  = t.status    





"""