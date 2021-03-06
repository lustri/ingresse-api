from api import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80))
	last_name = db.Column(db.String(80))
	age = db.Column(db.Integer)
	address = db.Column(db.String(255))
	
	def __init__(self, first_name, last_name, age, address):
		self.first_name = first_name;
		self.last_name = last_name;
		self.age = age;
		self.address = address;
