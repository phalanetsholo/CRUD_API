from urllib import request
from flask import Blueprint, jsonify
from database import get_db_connection 
from flask import Blueprint



user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def get_employees():
    conn = get_db_connection()  
    cur = conn.cursor()  
    cur.execute('SELECT * FROM employees;')  
    employees = cur.fetchall()  
    conn.close()  
    return jsonify(employees)  

@user_bp.route('/', methods=['POST'])
def add_employee():
    data = request.get_json()  
    first_name = data['first_name']
    last_name = data['last_name']


    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO employees (first_name, last_name) VALUES (%s, %s)', 
        (first_name, last_name)
    )  
    conn.commit()  
    conn.close()  
    return jsonify({"message": "Employee added successfully!"}), 201 

@user_bp.route('/', methods=['PUT'])
def update_employee(id):
    data = request.get_json()   
    first_name = data['first_name']
    last_name = data['last_name']
    

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE employees SET first_name = %s, last_name = %s WHERE id = %s',
        (first_name, last_name, id)
    ) 
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee updated successfully!"})

@user_bp.route('/', methods=['DELETE'])
def delete_employee(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM employees WHERE id = %s', (id,))  
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee deleted successfully!"})




