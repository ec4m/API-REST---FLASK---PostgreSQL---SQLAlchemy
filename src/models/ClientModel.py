from database.db import db

class ClientModel(db.Model):
  __tablename__ = 'client'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  lastname = db.Column(db.String(50))
  age = db.Column(db.Integer)


  def __init__(self, name, lastname, age):
    self.name = name
    self.lastname = lastname
    self.age = age