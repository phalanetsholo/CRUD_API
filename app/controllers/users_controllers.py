from app.models.users_models import Employee

class EmployeeController:
    @staticmethod
    def get_all_employees():
        employees = Employee.get_all_employees()
        return {'employees': employees}, 200

    @staticmethod
    def add_employee(name, position, salary):
        
        success = Employee.add_employee(name, position, salary)
        if success:
            return {'message': 'Employee added successfully'}, 201
        return {'message': 'Error adding employee'}, 500
    
    @staticmethod
    def update_employee(name, position, salary, id):
        success = Employee.update_employee(name, position, salary,id)
        if success:
            return{'message': 'Employee updated successfully'}, 201
        return {'message': 'Error updating employee'}, 500

    @staticmethod
    def delete_employee(employee_id):
        success = Employee.delete_employee(employee_id)
        if success:
            return {'message': 'Employee deleted successfully'}, 200
        return {'message': 'Error deleting employee'}, 500
