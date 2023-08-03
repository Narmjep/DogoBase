from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database import *
import random
from rng import *

api = Api()

# ------ Creating ------ #

DogCreate_args = reqparse.RequestParser()
DogCreate_args.add_argument('id', type=int, help='Unique ID of the dog')
DogCreate_args.add_argument('name', type=str, help='Name of the dog')
DogCreate_args.add_argument('gender' , type=str , help='Gender of the dog. Either male or female')

class DogCreate(Resource):
    @marshal_with(Dog_Resource_Fields)
    def post(self):
        print("PUT request received")
        args = DogCreate_args.parse_args()
        # Check if id was given
        id = args.get('id')
        #Check if id is valid
        if not _is_id_valid(id):
            id = _get_new_id()
        # Check if gender was given
        gender = args.get('gender')
        if not gender or gender not in ('male' , 'female'):
            # Chose gender randomly
            rn = random.randint(0, 1)
            if rn == 0:
                gender = 'male'
            else:
                gender = 'female'

        # Check if name was given
        name = args.get('name')
        if not name:
            if gender == 'male':
                name = get_random_male_name()
            else:
                name = get_random_female_name()

        # Create new dog
        dog = DogModel(id=id , name=name, gender=gender)
        print(f"Created new dog: {dog}")
        # Add dog to database
        db.session.add(dog)
        db.session.commit()
        return dog , 201

api.add_resource(DogCreate,'/api/create')

#  --------- Searching ---------  #

# Searching with URL params

class DogSearchByIndex(Resource):
    @marshal_with(Dog_Resource_Fields)
    def get(self, identifier):
        print("GET request")
        
        if identifier == '*':
            print("GET all request")
            dogs = DogModel.query.all()
            return dogs
        else:
            print(f"ID: {identifier}")
            dog = DogModel.query.filter_by(id=identifier).first()
            if not dog:
                abort(404, message='Could not find a dog with that id')
            return dog

api.add_resource(DogSearchByIndex, '/api/search/<string:identifier>')

# Searching with GET json params

dogSearch_args = reqparse.RequestParser()
dogSearch_args.add_argument('id', type=str, help='Name of the dog')
dogSearch_args.add_argument('name', type=str, help='Name of the dog')
dogSearch_args.add_argument('gender', type=str, help='Gender of the dog. Either male or female')

class DogSearch(Resource):
    @marshal_with(Dog_Resource_Fields)
    def get(self):
        args = dogSearch_args.parse_args()
        id = args.get('id')
        name = args.get('name')
        gender = args.get('gender')
        # Create an sql query
        query = DogModel.query
        if id:
            query = query.filter_by(id=id)
        if name:
            query = query.filter_by(name=name)
        if gender:
            query = query.filter_by(gender=gender)
        
        return query.all()

api.add_resource(DogSearch , '/api/search')

# SQL search

dogSearchSQL_args = reqparse.RequestParser()
dogSearchSQL_args.add_argument('query', type=str, help='A SQL query to search for dogs')

class DogSearchSQL(Resource):
    @marshal_with(Dog_Resource_Fields)
    def get(self):
        args = dogSearchSQL_args.parse_args()
        query = args.get('query')
        print("Query: " + query)
        if not query:
            abort(404, message='No query given')
        # Create an sql query
        dogs = db.session.execute(text(query))
        return dogs.all()

api.add_resource(DogSearchSQL , '/api/sql')



def _is_id_valid(id):
    if not id:
        return False
    if not isinstance(id, int):
        return False
    if id < 0:
        return False
    if DogModel.query.filter_by(id=id).first():
        return False
    
    return True

def _get_new_id():
    # Find the highest id and add 1
    highest_id = 0
    for dog in DogModel.query.all():
        if dog.id > highest_id:
            highest_id = dog.id
    return highest_id + 1


