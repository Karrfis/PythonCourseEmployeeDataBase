# Assignment: Employee and Department Management System
Duration: ~1 hour
Skills Covered:<br> SQLite, Python, SQL Queries, SQLAlchemy, Foreign Keys, CRUD
Operations, Pandas, Visualization (matplotlib)<br>
Objective<br>
You will build a Python-based Employee and Department Management System using
SQLite.<br>
This system should allow users to:<br>
Add new departments and employees.<br>
View all employees with their department names.<br>
Update employee salary.<br>
Delete an employee.<br>
Display a department-wise employee count (with a visualization).<br>

# Assignment Tasks
1. Set Up the Database (10 min)<br>
Connect to an SQLite database company.db.<br>
Create the departments table.<br>
Create the employees table with a foreign key reference to departments.id.<br>
2. Implement CRUD Operations (30 min)<br>
Add New Department<br>
Allow the user to add a new department (if it doesn’t already exist).<br>
Add New Employee<br>
Allow the user to enter:<br>
Name, Age, Department (as text, map to department_id), Salary<br>
Store the employee in the database.<br>
Update Employee Salary<br>
Prompt the user to select an employee by ID and enter a new salary.<br>
Update the salary in the database.<br>
Delete an Employee<br>
Prompt the user for an employee ID and delete the employee from the database.<br>
View All Employees with Department Names<br>
Retrieve and display all employees with department names (using JOIN).<br>
3. Perform Data Analysis & Visualization (20 min)<br>
Count Employees by Department<br>
Query how many employees are in each department.<br>
Display the count in a table format.<br>
Plot a Bar Chart<br>
Use Matplotlib to generate a bar chart of department-wise employee count.<br>
