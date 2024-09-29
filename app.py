from flask import Flask, render_template, request, redirect, abort
from models import db, EmployeeModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_tables():
    # The following line will remove this handler, making it
    # only run on the first request
    app.before_request_funcs[None].remove(create_tables)

    db.create_all()



@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def retrieve_list():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html', employees=employees)

@app.route('/data/<int:id>')
def RetrieveEmployee(id):
    employee = EmployeeModel.query.get(id)  # Use the primary key instead
    if employee:
        return render_template('data.html', employee=employee)
    return f"Employee with id = {id} doesn't exist", 404

@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    employee = EmployeeModel.query.get(id)  # ID ile sorgulama
    if request.method == 'POST':
        if employee:
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee.name = name
            employee.age = age
            employee.position = position
            db.session.commit()
            return redirect(f'/data/{id}')  # Burada doğrudan id kullanıyoruz
        return f"Employee with id={id} doesn't exist", 404

    return render_template('update.html', employee=employee)



@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        return f"Employee with id={id} doesn't exist", 404

    return render_template('delete.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
