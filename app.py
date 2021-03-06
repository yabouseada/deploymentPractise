import os
import re

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister, UserReview
from resources.item import Item,ItemList
from resources.store import Store,StoreList
from db import db

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= uri  #'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'yahia'
api= Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt= JWT(app,authenticate,identity) #/auth


api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserReview,'/review')
if __name__ == '__main__':
    app.run(port=5000,debug = True)
