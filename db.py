import sqlite3

def get_connection():
    return sqlite3.connect("employee.db")

def create_table (): 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name VARCHAR(70) NOT NULL,
    contact VARCHAR(15) UNIQUE NOT NULL,
    department VARCHAR(30) NOT NULL,
    salary INT NOT NULL
    )
    """) 

    conn.commit()
    conn.close()
create_table()