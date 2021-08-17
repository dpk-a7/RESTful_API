"""
_________________________________
|           WELCOME             |
|-------------------------------|
|RESTful API + JWT + CRUD + Hash|
|        by Deepak Avudiappan   |
|-------------------------------|
"""

from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
connect_ = os.getenv("URL")  # Add the mongo db url in .env file
cluster = MongoClient(connect_)
db = cluster['MyDB1']  # Change the db name

app = Flask(__name__)
app.config['SECRET_KEY'] = "53CR37KEY"


class Users():
    id = str()
    first = str()
    last = str()
    email = str()
    password = str()

    @classmethod
    def changeVar(cls, id, first_name, last_name, email, password):  # to change class variable
        cls.id = id
        cls.first = first_name
        cls.last = last_name
        cls.email = email
        cls.password = password


def usermaker(user):
    """
    Creates a Collection in mongo database
    """
    if user not in db.list_collection_names():
        Users = db.create_collection(user)


def token_required(f):
    """
    A wrapper function to authenticate JWT
    """

    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except Exception as e:
            return jsonify({'message': f'token is invalid: {e}'})
        user = Users()
        return f(user.first + '_' + user.last,*args, **kwargs)

    return decorator


@app.route('/register', methods=['POST'])
def register():
    """
    first_name, last_name_, email, password are required fields
    Note that I have used password ony from here, we can have another data base to store user credentials
    """
    args = request.get_json()
    try:
        if args['password'] != '':
            hashed_password = generate_password_hash(args['password'], method='sha256')
            user = Users()
            user.changeVar(id=str(uuid.uuid4()),
                           first_name=args["first_name"],
                           last_name=args["last_name"],
                           email=args["email"],
                           password=hashed_password)
            usermaker(f"{args['first_name']}_{args['last_name']}")
            return jsonify({
                'message': 'registered successfully',
                'Your user id': user.id,
                'Your user name': user.first + '_' + user.last
            })
    except:
        return jsonify({"error": "Please specify first_name, last_name_, email, password in a json format"})


@app.route('/login', methods=['POST'])
def login():
    """
    email and password are required fields
    """
    auth = request.authorization
    print(auth)
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
    user = Users()
    if check_password_hash(user.password, auth.password) and auth.username == user.first + '_' + user.last:
        token = jwt.encode(
            {'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


@app.route('/template', methods=['POST'])
@token_required
def Create(user_name):
    """
    Insert new template
    """
    args = request.get_json()
    try:
        U_col = db[user_name]
        id = U_col.count_documents({}) + 1
        temp = {
            '_id': id,
            'template_name': args['template_name'],
            'subject': args['subject'],
            'body': args['body'],
            'update_date': datetime.datetime.now(),
            'create_date': datetime.datetime.now()
        }
        n = U_col.insert_one(temp)
        return jsonify({args['template_name']: {"id": id}})
    except:
        return jsonify({"note":"Please include template_name, subject and body"})


@app.route('/template', methods=['GET'])
@token_required
def Read_all(user_name):
    """
    Get all template
    """
    U_col = db[user_name]
    results = U_col.find({})
    d = [result for result in results]
    return jsonify(d)


@app.route('/template/<int:template_id>', methods=['GET'])
@token_required
def Read_single(user_name, template_id):
    """
    Get single template
    """
    U_col = db[user_name]
    results = U_col.find({"_id": template_id})
    d = [result for result in results]
    return jsonify(d)


@app.route('/template/<int:template_id>', methods=['PUT'])
@token_required
def Update(user_name, template_id):
    """
    Update single template
    """
    args = request.get_json()
    U_col = db[user_name]
    args["update_date"] = datetime.datetime.now()
    result = U_col.update_one({"_id": template_id}, {"$set": args})
    return jsonify({"status": 200})


@app.route('/template/<int:template_id>', methods=['DELETE'])
@token_required
def Delete(user_name, template_id):
    """
    Delete single template
    """
    U_col = db[user_name]
    result = U_col.delete_one({"_id": template_id})
    return jsonify({"status": 200})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)  # debug=True
