from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text

app = Flask(__name__)

app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
#app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///new.db'
#app.config['SQLACHEMY_DATABASE_URI'] = 'jdbc:sqlite:///pin.db'

db = SQLAlchemy(app)


class Pin(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)

#app.debug = True

db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'

app.debug=True


if __name__ == '__main__':
    app.run()
