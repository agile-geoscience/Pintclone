# video at https://www.youtube.com/watch?v=2geC50roans
# tutorial done until 17"40'

from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from flask import send_from_directory
import os
from flask import request
from flask import jsonify, json
import goldenGoogleVision as ggv


application = Flask(__name__, static_url_path='')

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)


class Pin(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)
    tags = Column(Text, unique=False)
    html = Column(Text, unique=False)
    timestamp = Column(Text, unique=False)
    locations = Column(Text, unique=False)
    insights = Column(Text, unique=False)
    img_dict = Column(Text, unique=False)
    url = Column(Text, unique=False)

    def __init__(self, title, image, tags, html, 
    				timestamp, locations, insights, img_dict, url):
        self.title = title
        self.image = image
        self.tags = tags
        self.html = html
        self.timestamp = timestamp
        self.locations = locations
        self.insights = insights
        self.img_dict = img_dict
        self.url = url

# class Pin2(db.Model):
#     id = Column(Integer, primary_key=True)
#     title = Column(Text, unique=False)
#     image = Column(Text, unique=False)
#     tags = Column(Text, unique=False) 
#     html = Column(Text, unique=False) 
#     timestamp = Column(Text, unique=False) 


db.create_all()

api_manager = APIManager(application, flask_sqlalchemy_db=db)
api_manager.create_api(Pin, methods=['GET', 'POST', 'DELETE', 'PUT'])
# api_manager.create_api(Pin2, methods=['POST'])
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


@application.route('/store', methods=['POST'])
def create_task():

    d = request.data.decode()
    j = json.loads(d)


    url = j['url']
    title = j['title']
    image = j['image']
    tags = j['tags']
    html = j['html']
    timestamp = j['timestamp']
    locations = ''
    insights = ''
    img_dict = ''
    
    locations,image = ggv.getImsMakeThumb(title)
    
    thing = Pin(title, image, tags, html, timestamp,locations,insights,img_dict)

    db.session.add(thing)
    db.session.commit()

    return "success", 201

@application.route('/gvis', methods=['POST'])
def run_google():

    d = request.data.decode()
    j = json.loads(d)

    ts = str(j['timestamp'])

    print(ts)

    fields = Pin.query.filter_by(timestamp=ts).first()

    print(fields.id)
    
    
    # thing = Pin(title, image, tags, html, timestamp)

    # db.session.add(thing)
    # db.session.commit()

    return "success", 201


application.debug = True


if __name__ == '__main__':
    application.run()
