from database.db import db

class PetModel(db.Model):
  __tablename__ = 'Pet'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  race = db.Column(db.String(50))


  def __init__(self, name, race):
    self.name = name
    self.race = race