from db import get_connection

def insert_default_employees():
    conn = get_connection()
    cursor = conn.cursor()

    employees = [
        (106, "Aman", "9991110001", "IT", 60000),
        (107, "Riya", "9991110002", "HR", 45000),
        (108, "Kunal", "9991110003", "Finance", 70000),
        (109, "Neha", "9991110004", "IT", 55000),
        (110, "Rahul", "9991110005", "Sales", 40000),
        (111, "Pooja", "9991110006", "HR", 48000),
        (112, "Arjun", "9991110007", "IT", 80000),
        (113, "Sneha", "9991110008", "Marketing", 42000),
        (114, "Vikas", "9991110009", "Finance", 75000),
        (115, "Anjali", "9991110010", "Sales", 50000)
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?)",
        employees
    )

    conn.commit()
    conn.close()


    print("Default employees inserted successfully!")



insert_default_employees()
