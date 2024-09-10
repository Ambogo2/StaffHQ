"""Database models"""
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
from datetime import datetime
from sqlalchemy import Enum


class Employee(db.model):
    __tablename__ = 'employees'

    users_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        """Hashes passwords"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """checks the password hash"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<Employee {self.name}>'
    
class role(db.model):
    __tablename__="role"
    role_name= db.Column(db.String(100), nullable=False)
    description= db.Column(db.String(256), nullable=False)
    user_id= db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)

class LeaveRequest(db.Model):
    __tablename__ = 'leave_request'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    leave_type = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True)
    schedule_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(256), nullable=False)
    status = db.Column(Enum('Pending', 'Confirmed', 'Cancelled', name='status_enum'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Appointment {self.id} - {self.status}>"

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
 

class SearchLog(db.Model):
    __tablename__ = 'searchlog'
    id = db.Column(db.Integer, primary_key=True)
