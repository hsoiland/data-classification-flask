from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Credit(db.Model):
    __tablename__ = 'creditclassified'
    __table_args__ = {"schema":"creditschema"}

    id = db.Column('id', db.Integer, primary_key = True)
    classification = db.Column('classification', db.Integer)
   