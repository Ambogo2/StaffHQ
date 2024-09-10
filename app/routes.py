from flask import Flask, jsonify, request
from config import db
from werkzeug.security import check_password_hash
import os
from models import Employee

app = Flask(__name__)

# Creates an employee with hashed password
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = Employee(
        name=data['name'],
        email=data['email'],
        department=data['department'],
        role=data['role']
    )
    new_employee.set_password(data['password'])  # Hash the password
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee created successfully'}), 201

# Gets all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        'id': e.id,
        'name': e.name,
        'email': e.email,
        'department': e.department,
        'role': e.role
    } for e in employees]), 200

# Get a single employee
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify({
        'id': employee.id,
        'name': employee.name,
        'email': employee.email,
        'department': employee.department,
        'role': employee.role
    }), 200

# Update an employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    employee = Employee.query.get_or_404(id)
    employee.name = data['name']
    employee.email = data['email']
    employee.department = data['department']
    employee.role = data['role']
    db.session.commit()
    return jsonify({'message': 'Employee updated successfully'}), 200

# Delete an employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted successfully'}), 200

# Endpoint for user login
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the employee by email
    employee = Employee.query.filter_by(email=email).first()

    # If employee not found or password doesn't match, return error
    if not employee or not employee.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Login successful - For now just return a success message
    # (Later, you'd want to return a token or create a session)
    return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
