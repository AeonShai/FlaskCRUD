from app import app, db, EmployeeModel  # 'your_app_name' kısmını uygulamanızın ismiyle değiştirin

# Uygulama bağlamını başlat
with app.app_context():
    # Veritabanındaki tüm çalışanları al
    employees = EmployeeModel.query.all()

    # Çalışanları yazdır
    for emp in employees:
        print(emp.id, emp.name)
