import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="student",     
            user="postgres",           
            password="Riju@1111",   
            host="localhost",
            port="5432"
        )
        print("✅ Connection successful!")
        return conn
    except Exception as e:
        print(f"❌ Connection failed:", e)
        return None 
    
def insert_student(conn, name, age, department, email):
    cursor = conn.cursor()
    query = """INSERT INTO student_schema.students (name, age, department, email)
               VALUES (%s, %s, %s, %s);"""
    cursor.execute(query, (name, age, department, email))
    conn.commit()
    cursor.close()
    print("✅ Student inserted successfully!")

def fetch_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_schema.students;")
    rows = cursor.fetchall()
    cursor.close()
    return rows   

def update_student_age(conn, student_id, new_age):
    cursor = conn.cursor()
    query = """UPDATE student_schema.students
               SET age = %s WHERE student_id = %s;"""
    cursor.execute(query, (new_age, student_id))
    conn.commit()
    cursor.close()
    print("✅ Student updated successfully!")

def delete_student(conn, student_id):
    cursor = conn.cursor()
    query = "DELETE FROM student_schema.students WHERE student_id = %s;"
    cursor.execute(query, (student_id,))
    conn.commit()
    cursor.close()
    print("✅ Student deleted successfully!")




import json

def export_to_json(conn, filename="students.json"):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_schema.students;")
    rows = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]
    

    data = [dict(zip(col_names, row)) for row in rows]
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    cursor.close()
    print(f"✅ Data exported to {filename}")


import json

def export_to_json(conn, filename="students.json"):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_schema.students;")
    rows = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]
    
    # Convert rows to list of dicts
    data = [dict(zip(col_names, row)) for row in rows]
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    cursor.close()
    print(f"✅ Data exported to {filename}")

 

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        # Insert demo students
        insert_student(conn, "Alan", 21, "Cs", "An@gmail.com")
        insert_student(conn, "Venaly", 22, "Electronic", "Ve@gmail.com")
        
  
        students = fetch_students(conn)
        print("\n📚 Student Records:", students)
        
        # Update a student
        update_student_age(conn, 1, 33)
        delete_student(conn, 2)
        # Export to JSON
        export_to_json(conn)
        
        conn.close()

    conn = connect_db()
    if conn:
        insert_student(conn, "mr.k", 21, "Mechanical", "k@example.com")
        insert_student(conn, "mr.m", 22, "Sociology", "m@example.com")
        export_to_json(conn)
        conn.close()

