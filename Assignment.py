import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///company.db")
Session = sessionmaker(bind=engine)
session = Session()
conn = sqlite3.connect("company.db")
cursor = conn.cursor()


from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
Base = declarative_base()
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))
    salary = Column(Float)

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
Base.metadata.create_all(engine)
## showing off my using two libraries for no reason eheheehehehehe
##_____________________________________________________________________________________
## view department
##_____________________________________________________________________________________

def view_departments():
    cursor.execute("SELECT name FROM departments")
    departments = cursor.fetchall()
    if not departments:
        print("\nNo departments found.\n")
    else:
        print("\nCurrent Departments:")
        for dept in departments:
            print("- " , dept[0])
##_____________________________________________________________________________________
## add department
##_________________________________________________________________________________
def add_department():
    view_departments()
    name = input("Enter Department Name: ")
    cursor.execute("SELECT name FROM departments WHERE name = ?", (name.lower(),))
    if cursor.fetchone():
        print(f"\nDepartment {name} already exists.\n")
        return
    cursor.execute("INSERT INTO departments (name) VALUES(?)", (name.lower(),))
    conn.commit()
    print(f"\ndepartment {name} added successfully!\n")
##_____________________________________________________________________________________
## employee
##_____________________________________________________________________________________
def add_employee():
    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("\nInvalid age. Please enter a numeric value.\n")
        return        
    department_id = int(input("Enter department ID: "))
    cursor.execute("SELECT id FROM departments")
    department_ids = [dept[0] for dept in cursor.fetchall()]
    if department_id not in department_ids:
        print("\nInvalid department ID. Please enter a valid department ID.\n")
        return
    try:
        salary = float(input("Enter salary: "))
    except ValueError:
        print("\nInvalid salary. Please enter a numeric value.\n")
        return
    cursor.execute("INSERT INTO employees (name, age, department_id, salary) VALUES(?, ?, ?, ?)", (name, age, department_id, salary))
    conn.commit()
    print(f"\nEmployee {name} added successfully!\n")
##_____________________________________________________________________________________
# view employee
##_____________________________________________________________________________________
def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    if not employees:
        print("\nNo employees found.\n")
    else:
        print("\nEmployee List:")
    for emp in employees:
        print(emp) 
##_____________________________________________________________________________________
## update employee
##_____________________________________________________________________________________

def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    employee = cursor.fetchone()
    if not employee:
        print("\nEmployee not found!\n")
        return
    print("\nUpdating Employee:", employee)
    # update name
    name = input("Enter new name (or press Enter to keep the same): ") or employee[1]

    # update age
    while True:
        age = input("Enter new age (or press Enter to keep the same): ")
        if age == "":
            age = employee[2]
            break
        try:
            age = int(age)
            break
        except ValueError:
            print("\nInvalid age. Please enter a numeric value.\n")

    #update department
    while True:
        department_id = input("Enter new department ID (or press Enter to keep the same): ") or employee[3]
        if department_id == employee[3]:
            break
        cursor.execute("SELECT id FROM departments WHERE id = ?", (department_id,))
        if cursor.fetchone():
            break
        else:
            print("\nInvalid department ID. Please enter a valid department ID.\n")


    # update salary
    while True:
        salary = input("Enter new salary (or press Enter to keep the same): ") or employee[4]
        if salary == employee[4]:
            break
        try:
            salary = float(salary)
            break
        except ValueError:
            print("\nInvalid salary. Please enter a numeric value.\n")
    # push to database
    cursor.execute("UPDATE employees SET name = ?, age = ?, department_id = ?, salary = ? WHERE id = ?", (name, age, department_id, salary, emp_id))
    conn.commit()
    print(f"\nEmployee ID {emp_id} : {name} updated successfully!\n")
##_____________________________________________________________________________________
## delete employee
##_____________________________________________________________________________________
def delete_employee():
	emp_id = int(input("Enter Employee ID to delete: "))
	cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
	employee = cursor.fetchone()
	if not employee:
		print("\nEmployee not found!\n")
		return
	confirm = input(f"Are you sure you want to delete {employee[1]}? (y/n): ").lower()
	if confirm == "y":
		cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
		conn.commit()
		print(f"\nEmployee ID {emp_id} deleted successfully!\n")
	else:
		print("\nDelete action canceled.\n")

##_____________________________________________________________________________________
## view all employees 

def view_all_employees():
    cursor.execute("SELECT employees.id, employees.name, employees.age, departments.name, employees.salary FROM employees JOIN departments ON employees.department_id = departments.id")
    employeelist = cursor.fetchall()
    if not employeelist:
        print("\nNo employees found.\n")
    else:
        print("\nEmployee List:")
        for emp in employeelist:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}, Salary: £ {emp[4]}")
##_____________________________________________________________________________________
## employee department count dataframe

def employee_department_count():
    cursor.execute("SELECT departments.name, COUNT(employees.id) FROM employees JOIN departments ON employees.department_id = departments.id GROUP BY departments.name")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["Department", "Employee Count"])

    if df.empty:
        print("\nNo data available to plot.\n")
        return
    df.plot(kind='bar', x='Department', y='Employee Count', legend=False)
    plt.title('Number of Employees in Each Department')
    plt.xlabel('Department')
    plt.ylabel('Employee Count')
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    plt.tight_layout()
    plt.show()
##_____________________________________________________________________________________  
## menu
##_____________________________________________________________________________________
def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add New Department")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. View All Employees")
        print("7. View Employee Department Count")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_department()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            view_all_employees()
        elif choice == "7":
            employee_department_count()
        elif choice == "8":
            print("\nExiting")
            conn.close()
            break
        else:
            print("\nInvalid Choice, Please Try again \n")

# Run the menu
menu()