from flask import Blueprint, request, jsonify

# Database
from database.db import db
# Models
from models.OrdenModel import OrdenModel

orden = Blueprint('orden', __name__)


@orden.route('/')
def get_ordenes():
  try:
    ordenes = OrdenModel.query.all()
    list = []
    for orden in ordenes:
      list.append({
        "id": orden.id,
        "date": orden.date,
        "client_id": orden.client_id,
        "product_id": orden.product_id,
      })
    return jsonify(list)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@orden.route('/<id>')
def get_orden(id):
  try:
    orden = OrdenModel.query.get(id)
    if orden != None:
      return jsonify({
        "id": orden.id,
        "date": orden.date,
        "client_id": orden.client_id,
        "product_id": orden.product_id,
      })
    return jsonify({'message': 'Orden not found.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})


@orden.route('/add', methods=['POST'])
def add_orden():
  try:
    date = request.json['date']
    client_id = request.json['client_id']
    product_id = request.json['product_id']
    orden = OrdenModel(date, client_id, product_id)

    db.session.add(orden)
    db.session.commit()

    return jsonify({
      "id": orden.id,
      "date": orden.date,
      "client_id": orden.client_id,
      "product_id": orden.product_id
    })
  except Exception as ex:
    return jsonify({'message': str(ex)})


@orden.route('/delete/<id>', methods=['DELETE'])
def delete_orden(id):
  try:
    orden = OrdenModel.query.get(id)
    if orden != None:
      db.session.delete(orden)
      db.session.commit()
      return jsonify({
        "id": orden.id,
        "date": orden.date,
        "client_id": orden.client_id,
        "product_id": orden.product_id,
      })
    return jsonify({'message': 'Orden not deleted.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})

@orden.route('/update/<id>', methods=['PUT'])
def update_orden(id):
  try:
    orden = OrdenModel.query.get(id)
    if orden != None:
      orden.date = request.json['date']
      orden.client_id = request.json['client_id']
      orden.product_id = request.json['product_id']
      db.session.commit()
      return jsonify({
        "id": orden.id,
        "date": orden.date,
        "client_id": orden.client_id,
        "product_id": orden.product_id
      })
    return jsonify({'message': 'Orden not updated.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})