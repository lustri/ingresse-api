import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from api import db, app
from api.register.models import User

register = Blueprint('register', __name__)

@register.route('/')
@register.route('/home')
def home():
    return "Welcome to the Register Home."

class UserView(MethodView):

	def get(self, id=None):
		if not id:
			users = User.query.all()
			res = {}
			for user in users:
				res[user.id]= {
					'first_name': user.first_name,
					'last_name': user.last_name,
					'age': str(user.age),
					'address': user.address,
				}
		else:
			user = User.query.filter_by(id=id).first()
			if not user:
				abort(404)
			res = {
				'first_name': user.first_name,
				'last_name': user.last_name,
				'age': str(user.age),
				'address': user.address,
			}
		return jsonify(res)

	def post(self):
		first_name = request.form.get('first_name')
		last_name = request.form.get('last_name')
		age = request.form.get('age')
		address = request.form.get('address')
		user = User(first_name, last_name, age, address)
		db.session.add(user)
		db.session.commit()
		return jsonify({user.id: {
			'first_name': user.first_name,
			'last_name': user.last_name,
			'age': str(user.age),
			'address': user.address,
		}})

	def put(self, id):
		user = User.query.filter_by(id=id).first()
		if not user:
			abort(404)
		first_name = request.form.get('first_name')
		last_name = request.form.get('last_name')
		age = request.form.get('age')
		address = request.form.get('address')
		if first_name is not None:
			user.first_name = first_name
		if last_name is not None:
			user.last_name = last_name
		if age is not None:
			user.age = age
		if address is not None:
			user.address = address
		db.session.commit()
		return jsonify({user.id: {
			'first_name': user.first_name,
			'last_name': user.last_name,
			'age': str(user.age),
			'address': user.address,
		}})

	def delete(self, id):
		user = User.query.filter_by(id=id).first()
		if not user:
			abort(404)
		db.session.delete(user)
		db.session.commit()
		return jsonify({user.id: {
			'first_name': user.first_name,
			'last_name': user.last_name,
			'age': str(user.age),
			'address': user.address,
		}})

user_view = UserView.as_view('user_view')
app.add_url_rule(
	'/users/', view_func=user_view, methods=['GET','POST']
)
app.add_url_rule(
	'/users/<int:id>', view_func=user_view, methods=['GET','PUT','DELETE']	
)
