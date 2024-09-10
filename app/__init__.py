# initialize a Flask app and bind it to db
from flask import Flask
from .config import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pswd1234@localhost/employee_management'
    db.init_app(app)
    
    # Import and register blueprints, routes, etc.
    
    return app
