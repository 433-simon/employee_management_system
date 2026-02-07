from db import get_connection

def add_employee() :
        print("Add employee selected ")
        emp_id = int(input("Enter employee's id : "))
        emp_name = input("Enter employees' name : ")
        emp_contact = input("Enter employee's contact number : ")
        emp_department = input("Enter employee's department : ")
        emp_salary = int(input("Enter Employees's salary : "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
                """
                INSERT INTO employees (id,name,contact,department,salary)
                VALUES (?,?,?,?,?)
                """, 
                (emp_id,emp_name,emp_contact,emp_department,emp_salary)
        )

        conn.commit()
        conn.close()

        print("Employee Added Successfully!")

def view_all_employee():
        print("View Employee Selected ")
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute (
                """
                SELECT * FROM employees
                """
        )
        employees = cursor.fetchall()
        if len(employees) == 0:
                print("No employee found!")
        else:
                print("\nID | NAME | CONTACT | DEPARTMENT | SALARY ")
                print("*" * 50 )

        for employee in employees :
                emp_id, emp_name, emp_contact, emp_department, emp_salary = employee
                print(emp_id, "|", emp_name, "|", emp_contact, "|", emp_department, "|", emp_salary)

        conn.commit()
        conn.close()

def view_employee_by_id():
        print("Add employee by id selected ")
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute (
                """
                SELECT id , name FROM employees
                """
        )
        employees = cursor.fetchall()
        if len(employees) == 0:
                print("No employee found!")
        else:
                print("ID | NAME")
                print("-" * 20)

                for employee in employees:
                        emp_id, emp_name = employee
                        print(emp_id, "|", emp_name)

        conn.close()

def update_employee_salary() :
        print("Update employee salary selected ")

        conn = get_connection()
        cursor = conn.cursor()

        emp_id = int(input("Enter empoyee's id : "))
        updated_salary = int(input("Enter Updated salary :  "))

        cursor.execute(
                """
        UPDATE employees
        SET salary = ?
        WHERE  id = ?
                """, 
                (updated_salary , emp_id)
        )

        print("Salary Updated Successfully!")

        conn.commit()
        conn.close()


        
def delete_employee() :
        print("Delete Employee Selected ")


        conn = get_connection()
        cursor = conn.cursor()

        emp_id = int(input("Enter which employee you have to delete : "))
        cursor.execute(
                """
                DELETE FROM employees
                WHERE id = ?
                """,
                (emp_id,)
        )
        conn.commit()
        print("Employee Deleted Successfully!")
        conn.close()

def department_wise_report() :
        print("Department Wise Report Selected")
        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute(
                """
                SELECT  department, COUNT(*) 
                FROM employees
                GROUP BY department
                """
        )

        records = cursor.fetchall()
        print("\nDepartment | Total Employees")
        print("-" * 30)
        for department, count in records:
                print(department, "|", count)
        conn.close()


def exit_program () :
        print("Exiting Program....Logged Out!")
        exit()
