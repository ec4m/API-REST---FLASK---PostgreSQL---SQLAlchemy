from database.db import db


class ProductModel(db.Model):
  __tablename__ = 'product'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  description = db.Column(db.String(300))
  price = db.Column(db.Integer)
  ordenes = db.relationship('OrdenModel')

  def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price