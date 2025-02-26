from app.models.db_models import get_db_connection

class Employee:
    @staticmethod
    def get_all_employees():
        conn = get_db_connection()
        if not conn:
            return []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees

    @staticmethod
    def add_employee(name, position, salary):
        conn = get_db_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)", (name, position, salary))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error adding employee: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def update_employee(name, position, salary, id):
        conn = get_db_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE employees SET name = %s, position = %s, salary = %s WHERE id = %s",
                (name, position, salary, id)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating employee: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_employee(employee_id):
        conn = get_db_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting employee: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
