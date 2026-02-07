from operations import (
    add_employee,
    view_all_employee,
    view_employee_by_id,
    update_employee_salary,
    delete_employee,
    department_wise_report,
    exit_program
)

print("====== EMPLOYEE MANAGEMENT SYSTEM ======")

while True:
    print('''
Please Select an Option :
1. Add Employee
2. View All Employee
3. View Employee by ID
4. Update Employee Salary
5. Delete Employee
6. Department - Wise Report
7. Exit
''')

    choice = input("Enter your choice : ")
    print("DEBUG choice =", repr(choice))


    menu_actions = {
        "1": add_employee,
        "2": view_all_employee,
        "3": view_employee_by_id,
        "4": update_employee_salary,
        "5": delete_employee,
        "6": department_wise_report,
        "7": exit_program
    }

    action = menu_actions.get(choice)

    if action:
        action()
    else:
        print("Invalid choice")
