# video at https://www.youtube.com/watch?v=2geC50roans
# tutorial done until 17"40'

from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from flask import send_from_directory
import os


application = Flask(__name__, static_url_path='')

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


@application.route('/about')
def about():
    return application.send_static_file("about.html")


@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


application.debug = True


if __name__ == '__main__':
    application.run()
