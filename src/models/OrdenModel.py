from database.db import db

class OrdenModel(db.Model):
  __tablename__ = 'orden'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.String(50))
  client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


  def __init__(self, date, client_id, product_id):
    self.date = date
    self.client_id = client_id
    self.product_id = product_id