# Assignment: Employee and Department Management System
Duration: ~1 hour
Skills Covered: SQLite, Python, SQL Queries, SQLAlchemy, Foreign Keys, CRUD
Operations, Pandas, Visualization (matplotlib)
Objective
You will build a Python-based Employee and Department Management System using
SQLite. This system should allow users to:
Add new departments and employees.
View all employees with their department names.
Update employee salary.
Delete an employee.
Display a department-wise employee count (with a visualization).

# Assignment Tasks
1. Set Up the Database (10 min)
Connect to an SQLite database company.db.
Create the departments table.
Create the employees table with a foreign key reference to departments.id.
2. Implement CRUD Operations (30 min)
Add New Department
Allow the user to add a new department (if it doesn’t already exist).
Add New Employee
Allow the user to enter:
Name, Age, Department (as text, map to department_id), Salary
Store the employee in the database.
Update Employee Salary
Prompt the user to select an employee by ID and enter a new salary.
Update the salary in the database.
Delete an Employee
Prompt the user for an employee ID and delete the employee from the database.
View All Employees with Department Names
Retrieve and display all employees with department names (using JOIN).
3. Perform Data Analysis & Visualization (20 min)
Count Employees by Department
Query how many employees are in each department.
Display the count in a table format.
Plot a Bar Chart
Use Matplotlib to generate a bar chart of department-wise employee count.
