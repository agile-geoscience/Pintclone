# -*- coding: utf-8 -*-
import os

from sqlalchemy import Column, Integer, Text
from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
from flask import request
from flask import json

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
    auto_tags = Column(Text, unique=False)

    def __init__(self, title, image, tags, html,
                 timestamp, locations, insights, img_dict, url, auto_tags):
        self.title = title
        self.image = image
        self.tags = tags
        self.html = html
        self.timestamp = timestamp
        self.locations = locations
        self.insights = insights
        self.img_dict = img_dict
        self.url = url
        self.auto_tags = auto_tags

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
    auto_tags = ''

    # create optimal thumbnail from url, scrape title
    title, image = ggv.getImsMakeThumb(url)

    # save
    thing = Pin(title, image, tags, html, timestamp, locations, insights, img_dict, url, auto_tags)
    db.session.add(thing)
    db.session.commit()

    return timestamp, 201


@application.route('/gvis', methods=['POST'])
def run_google():

    d = request.data.decode()
    j = json.loads(d)

    ts = j['timestamp']

    fields = Pin.query.filter_by(timestamp=ts).last()

    url = fields.url
    # currenttags = fields.tags

    dic = ggv.scrapeImages(url)
    # print(dic)
    meaning = ggv.scrapeText(url)

    fields.locations = ",".join(dic[1])
    fields.auto_tags = " ".join(dic[2])+" "+" ".join(meaning[0])

    # thing = Pin(title, image, tags, html, timestamp)

    # db.session.add(thing)
    db.session.commit()

    return "success", 201


application.debug = True


if __name__ == '__main__':
    application.run()
