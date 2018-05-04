from flask import Flask, render_template, request, flash, redirect, session, abort
from flask_sqlalchemy import SQLAlchemy
from models import db, app, Credit
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/creditdb' 

@app.route("/")
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('index.html', credit = Credit.query.all())

@app.route("/login", methods=['POST'])
def do_admin_login():
	
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])

	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
	result = query.first()
	if result:
		session['logged_in'] = True
	else:
		return render_template("404.html")
	return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()


@app.route("/search", methods=['GET', 'POST'])
def search():
	text = request.form['query']
	credits = Credit.query.filter_by(id=text).first_or_404()
	
	return render_template('results.html', credits=credits)

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run()
