from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DBUSER = 'lustri'
DBPASS = 'lustri'
DBHOST = 'postgres'
DBPORT = '5432'
DBNAME = 'db'

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(user=DBUSER,
            passwd=DBPASS, host=DBHOST, port=DBPORT, db=DBNAME)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'lustri'

    db.init_app(app)

    from api.register.views import register, user_view
    app.register_blueprint(register)

    app.add_url_rule(
        '/users/', view_func=user_view, methods=['GET','POST']
    )
    app.add_url_rule(
        '/users/<int:id>', view_func=user_view, methods=['GET','PUT','DELETE']  
    )

    return app