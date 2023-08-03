from flask_restful import fields
from flask_sqlalchemy import SQLAlchemy
from server import app
from os import getcwd


db = SQLAlchemy()

# Dog table
class DogModel(db.Model):
    #name,gender = None,None    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100) , nullable=False)

    def __repr__(self):
        return f"({id} , {self.name} , {self.gender})"



Dog_Resource_Fields = {
    'id': fields.Integer,
    'name': fields.String,
    'gender': fields.String
}

