import unittest
import coverage
from flask_script import Manager

from api import create_app, db

#Coverage
cov = coverage.coverage(
	include='api/*',
	omit=[
		'test/*',
		'project/api/*'])
cov.start()

# Cria a aplicação flask
app = create_app()

#Manager permite rodar comandos enquanto a aplicação roda
manager = Manager(app)

#Criação dos modelos
import api.register
db.create_all(app=app)

@manager.command
def test():

	test = unittest.TestLoader().discover('test')
	result = unittest.TextTestRunner(verbosity=2).run(test)
	if result.wasSuccessful():
		cov.stop()
		cov.save()
		cov.report()
		cov.html_report()
		cov.erase()
		return 0
	else:
		return 1

#Roda a aplicação flask
if __name__ == '__main__':
	manager.run()