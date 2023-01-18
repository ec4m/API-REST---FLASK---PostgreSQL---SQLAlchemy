from database.db import db

class PetModel(db.Model):
  __tablename__ = 'pet'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  race = db.Column(db.String(50))
  users = db.relationship('UserModel')


  def __init__(self, name, race):
    self.name = name
    self.race = race