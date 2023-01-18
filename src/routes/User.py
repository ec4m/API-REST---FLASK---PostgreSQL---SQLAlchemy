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
        "id": user.id,
        "username": user.username,
        "name": user.name,
        "lastname": user.lastname,
        "password": user.password,
        "pet_id": user.pet_id,
      })
    return jsonify(list)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@user.route('/<id>')
def get_user(id):
  try:
    user = UserModel.query.get(id)
    if user != None:
      return jsonify({
        "id": id,
        "username": user.username,
        "name": user.name,
        "lastname": user.lastname,
        "password": user.password,
        "pet_id": user.pet_id,
      })
    return jsonify({'message': 'User not found.'})
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
      "id": user.id,
      "username": user.username,
      "name": user.name,
      "lastname": user.lastname,
      "password": user.password,
      "pet_id": user.pet_id,
    })

  except Exception as ex:
    return jsonify({'message': str(ex)})


@user.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = UserModel.query.get(id)
    if user != None:
      db.session.delete(user)
      db.session.commit()
      return jsonify({
        "username": user.username,
        "name": user.name,
        "lastname": user.lastname,
        "password": user.password,
        "pet_id": user.pet_id,
      })
    return jsonify({'message': 'User not deleted.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})


@user.route('/update/<id>', methods=['PUT'])
def update_user(id):
  try:
    user = UserModel.query.get(id)
    if user != None:
      user.username = request.json['username']
      user.name = request.json['name']
      user.lastname = request.json['lastname']
      user.password = request.json['password']
      user.pet_id = request.json['pet_id']
      db.session.commit()
      return jsonify({
        "id": user.id,
        "username": user.username,
        "name": user.name,
        "lastname": user.lastname,
        "password": user.password,
        "pet_id": user.pet_id,
      })
    return jsonify({'message': 'User not updated.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})