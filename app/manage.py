import unittest
from flask_script import Manager

from api import create_app, db

# Cria a aplicação flask
app = create_app()

#Manager permite rodar comandos enquanto a aplicação roda
manager = Manager(app)

import api.register
db.create_all(app=app)

@manager.command
def test():

	test = unittest.TestLoader().discover('test')
	result = unittest.TextTestRunner(verbosity=2).run(test)
	if result.wasSuccessful():
		return 0
	else:
		return 1

#Roda a aplicação flask
if __name__ == '__main__':
	manager.run()