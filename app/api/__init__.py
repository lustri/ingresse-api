from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DBUSER = 'lustri'
DBPASS = 'lustri'
DBHOST = '192.168.99.100'
DBPORT = '5432'
DBNAME = 'db'
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'lustri'

db = SQLAlchemy(app)
 
from api.register.views import register
app.register_blueprint(register)
 
db.create_all()
