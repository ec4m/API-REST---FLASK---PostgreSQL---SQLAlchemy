from flask import Blueprint, request, jsonify

# Database
from database.db import db
# Model
from models.PetModel import PetModel

pet = Blueprint('pet', __name__)


@pet.route('/')
def get_pets():
  try:
    pets = PetModel.query.all()
    list = []
    for pet in pets:
      list.append({
        "id": pet.id,
        "name": pet.name,
        "race": pet.race
      })
    return jsonify(list)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@pet.route('/<id>')
def get_pet(id):
  try:
    pet = PetModel.query.get(id)
    if pet != None:
      item = {
        "id": pet.id,
        "name": pet.name,
        "race": pet.race
      }
      return jsonify(item)
    return jsonify({'massage': 'Pet no found.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})


@pet.route('/add', methods=['POST'])
def add_pet():
  try:
    name = request.json['name']
    race = request.json['race']
    pet = PetModel(name, race)
    db.session.add(pet)
    db.session.commit()
    item = {
      "name": name,
      "race": race,
    }
    return jsonify(item)

  except Exception as ex:
    return jsonify({'message': str(ex)})

  
@pet.route('/delete/<id>', methods=['DELETE'])
def delete_pet(id):
  try:
    pet = PetModel.query.get(id)
    if pet != None:
      db.session.delete(pet)
      db.session.commit()
      item = {
        "id": id,
        "name": pet.name,
        "race": pet.race
      }
      return jsonify(item)
    return jsonify({'message': 'Pet not found. Not deleted.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})

  
@pet.route('/update/<id>', methods=['PUT'])
def update_pet(id):
  try:
    pet = PetModel.query.get(id)
    if pet != None:
      pet.name = request.json['name']
      pet.race = request.json['race']
      db.session.commit()
      return jsonify({
        "id": id,
        "name": pet.name,
        "race": pet.race
      })
    return jsonify({'message': 'Pet not found. Not updated.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})