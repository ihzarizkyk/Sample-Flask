# import flask
from flask import (Flask, render_template, url_for, abort)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# buat variabel app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# buat class untuk membuat struktur table
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nama = db.Column(db.String(50),nullable=False)

	def __repr__(self):
		return "<User %r>" % self.id

	def __init__(self,nama):
		self.nama = nama
# buat route untuk url ("/") sebagai index / baseurl
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/tentang")
def tentang():
	return render_template("tentang.html")

@app.route("/kontak")
def kontak():
	return render_template("kontak.html")