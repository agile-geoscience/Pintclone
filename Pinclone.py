# video at https://www.youtube.com/watch?v=2geC50roans
# tutorial done until 17"40'

from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from flask import request, render_template


application = Flask(__name__, static_url_path='')

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'

db = SQLAlchemy(application)


class Pin(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)


db.create_all()

api_manager = APIManager(application, flask_sqlalchemy_db=db)
api_manager.create_api(Pin, methods=['GET', 'POST', 'DELETE', 'PUT'])
# Connect to http://127.0.0.1:5000/api/pin !

@application.route('/')
def index():
    return application.send_static_file("index.html")

application.debug = True

if __name__ == '__main__':
    application.run()
