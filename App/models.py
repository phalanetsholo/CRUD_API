from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    department = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'


