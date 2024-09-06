from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pswd1234@localhost/employee_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)