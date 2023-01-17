from flask import Blueprint, request, jsonify
from database.db import db

# Models
from models.ClientModel import ClientModel

client = Blueprint('client', __name__)


@client.route('/')
def get_clients():
  try:
    clients = ClientModel.query.all()
    list = []
    for client in clients:
      list.append({
        "id": client.id,
        "name": client.name,
        "lastname": client.lastname,
        "age": client.age
      })
    return jsonify(list)
  except Exception as ex:
    return jsonify({'mesagge': str(ex)})
  

@client.route('/<id>')
def get_client(id):
  try:
    client = ClientModel.query.get(id)
    if client != None:
      item = {
        "id": id,
        "name": client.name,
        "lastname": client.lastname,
        "age": client.age
      }
    else:
      item = []

    return (item)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@client.route('/add', methods=['POST'])
def add_client():
  try:
    name = request.json['name']
    lastname = request.json['lastname']
    age = request.json['age']

    client = ClientModel(name, lastname, age)

    db.session.add(client)
    db.session.commit()
    item = {
      "name": client.name,
      "lastname": client.lastname,
      "age": client.age
    }
    return jsonify(item)

  except Exception as ex:
    return jsonify({'message': str(ex)})


@client.route('/delete/<id>', methods=['DELETE'])
def delete_client(id):
  try:
    client = ClientModel.query.get(id)
    if client != None:
      db.session.delete(client)
      db.session.commit()
      return jsonify({'message': f'Item correspondiente al id "{id}" eliminado.'})
    else: 
      return jsonify({'message': 'Elemento no encontrado, no eliminado.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})


@client.route('/update/<id>', methods=['PUT'])
def update_client(id):
  try:
    client = ClientModel.query.get(id)
    if client != None:
      client.name = request.json['name']
      client.lastname = request.json['lastname']
      client.age = request.json['age']
      db.session.commit()

      item = {
        "name": client.name,
        "lastname": client.lastname,
        "age": client.age
      }
      return jsonify(item)
    else:
      return jsonify({'message': 'Elemento no encontrado, no actualizado.'})

  except Exception as ex:
    return jsonify({'message': str(ex)})