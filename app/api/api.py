from flask import Flask
app = Flask(__name__)


from urllib import response
from flask import Blueprint, request, jsonify, render_template
from app.helpers import token_required
from app.models import db, User, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/username', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    print("comin here")
    username = request.json['make']
    make = request.json['model']
    model = request.json['contents']
    contents = request.json['contents']
    user_token = current_user_token.token
    print(username)
    print(f'BIG TESTER: {current_user_token.token}')
    
    contact = Contact(username, make, model, contents)
    
    db.session.add(username)
    db.session.commit()
    
    response = contact_schema.dump(contact)
    return jsonify(response)
