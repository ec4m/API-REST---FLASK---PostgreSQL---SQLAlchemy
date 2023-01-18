from flask import Blueprint, request, jsonify

# Database
from database.db import db
# Models
from models.UserModel import UserModel

user = Blueprint('user', __name__)


@user.route('/')
def get_users():
  try:
    users = UserModel.query.all()
    list = []
    for user in users:
      list.append({
        "username": user.username,
        "name": user.name,
        "lastname": user.lastname,
        "password": user.password,
        "pet_id": user.pet_id,
      })
    return jsonify(list)
  except Exception as ex:
    return jsonify({'message': str(ex)})




@user.route('/add', methods=['POST'])
def add_user():
  try:
    username = request.json['username']
    name = request.json['name']
    lastname = request.json['lastname']
    password = request.json['password']
    pet_id = request.json['pet_id']
    user = UserModel(username, name, lastname, password, pet_id)

    db.session.add(user)
    db.session.commit()

    return jsonify({
      "username": user.username,
      "name": user.name,
      "lastname": user.lastname,
      "password": user.password,
      "pet_id": user.pet_id,
    })

  except Exception as ex:
    return jsonify({'message': str(ex)})