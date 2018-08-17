import unittest
import json

from flask import jsonify
from flask_testing import TestCase
from api import create_app, db

DBUSER = 'lustri'
DBPASS = 'lustri'
DBHOST = 'postgres'
DBPORT = '5432'
DBNAME = 'db_test'

app = create_app()

class TestApi(TestCase):

	def create_app(self):

		app.config['SQLALCHEMY_DATABASE_URI'] = \
		'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
			user=DBUSER,
			passwd=DBPASS,
			host=DBHOST,
			port=DBPORT,
			db=DBNAME)
		app.config['DEBUG'] = True
		app.config['TESTING'] = True

		return app

	def test_user_creation(self):
		res_post = self.client().post('/users/', data=self.user)
		self.assertEqual(res_post.status_code, 200)
		self.assertIn('Guilherme',str(res_post.data))

	def test_user_delete(self):
		res_post = self.client().post('/users/', data=self.user)
		self.assertEqual(res_post.status_code, 200)
		res_delete = self.client().delete('/users/1')
		self.assertEqual(res_delete.status_code, 200)
		res_get = self.client().get('/users/1')
		self.assertEqual(res_get.status_code,404)

	def test_user_get_by_id(self):
		res_post = self.client().post('/users/', data=self.user)
		self.assertEqual(res_post.status_code, 200)
		res_get = self.client().get('/users/1')
		self.assertEqual(res_get.status_code, 200)
		self.assertIn('Guilherme',str(res_get.data))

	def test_user_get_all_users(self):
		res_post = self.client().post('/users/', data=self.user)
		self.assertEqual(res_post.status_code, 200)
		res_get = self.client().get('/users/')
		self.assertEqual(res_get.status_code, 200)
		self.assertIn('Guilherme', str(res_get.data))

	def test_user_edit(self):
		res_post = self.client().post('/users/', data=self.user)
		self.assertEqual(res_post.status_code, 200)
		res_put = self.client().put('/users/1', 
			data ={
				"first_name" : "Lustri"
			})
		self.assertEqual(res_put.status_code,200)
		res_get = self.client().get('/users/')
		self.assertEqual(res_get.status_code, 200)
		self.assertIn('Lustri', str(res_get.data))

	def setUp(self):

		self.client = self.app.test_client
		self.user = {'first_name': 'Guilherme'}

		db.create_all()

	def tearDown(self):
		
		db.session.remove()
		db.drop_all()

	
# Roda os testes
if __name__ == '__main__':
	unittest.main()

