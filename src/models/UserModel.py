from database.db import db

class UserModel(db.Model):
  __tablename__ = 'usuario'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50))
  name = db.Column(db.String(50))
  lastname = db.Column(db.String(50))
  password = db.Column(db.String(50))
  pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))


  def __init__(self, username, name, lastname, password, pet_id):
    self.username = username
    self.name = name
    self.lastname = lastname
    self.password = password
    self.pet_id = pet_id