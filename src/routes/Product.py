from flask import Blueprint, request, jsonify

# Models
from models.ProductModel import ProductModel
# Database
from database.db import db

product = Blueprint('product', __name__)


@product.route('/')
def get_products():
  try:
    products = ProductModel.query.all()
    list = []
    for product in products:
      list.append({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price
      })
    return jsonify(list)

  except Exception as ex:
    return jsonify({'message': str(ex)})


@product.route('/<id>')
def get_product(id):
  try:
    product = ProductModel.query.get(id)
    if product != None:
      item = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
      }
      return jsonify(item)
    return jsonify({'message': 'Product not found.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})


@product.route('/add', methods=['POST'])
def add_product():
  try:
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    product = ProductModel(name, description, price)

    db.session.add(product)
    db.session.commit()

    item = {
      "id": product.id,
      "name": product.name,
      "description": product.description,
      "price": product.price
    }

    return jsonify(item)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@product.route('/delete/<id>', methods=['DELETE'])
def delete_product(id):
  try:
    product = ProductModel.query.get(id)
    if product != None:
      db.session.delete(product)
      db.session.commit()
      item = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price
      }
      return jsonify(item)
    return jsonify({'message': 'Product not deleted.'})

  except Exception as ex:
    return jsonify({'message': str(ex)})


@product.route('/update/<id>', methods=['PUT'])
def update_product(id):
  try:
    product = ProductModel.query.get(id)
    if product != None:
      product.name = request.json['name']
      product.description = request.json['description']
      product.price = request.json['price']
      db.session.commit()
      item = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price
      }
      return jsonify(item)
    return jsonify({'message': 'Product not found. Product not updated.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})