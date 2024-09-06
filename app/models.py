"""Database models"""

from config import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class Employee(db.model):
    __tablename__ = 'employees'

    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(100), nullable=False)
    email = db.column(db.string(100), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}>'
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
db.create_all() # creates tables in the database created