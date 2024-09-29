from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "employees"  

    id = db.Column(db.Integer, primary_key=True)  # Birincil anahtar
    employee_id = db.Column(db.Integer(), unique=True, nullable=False)  
    name = db.Column(db.String(), nullable=False)  
    age = db.Column(db.Integer(), nullable=False)  
    position = db.Column(db.String(80), nullable=False)  

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position


    def __repr__(self):
        return f"{self.name}: {self.employee_id}"
