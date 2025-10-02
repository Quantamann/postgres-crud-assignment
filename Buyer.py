import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="Buyer_data",      
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
    

def insert_data(conn, name, age, type, email):
    cursor = conn.cursor()
    query = """INSERT INTO buyer.data(name, age, type, email)
               VALUES (%s, %s, %s, %s);"""
    cursor.execute(query, (name, age, type, email))
    conn.commit()
    cursor.close()
    print("✅ Buyer inserted successfully!")    
    





def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buyer.data;")
    rows = cursor.fetchall()
    cursor.close()
    return rows

def update_buyer_age(conn, buyer_id, new_age):
    cursor = conn.cursor()
    query = """UPDATE buyer.data
               SET age = %s WHERE buyer_id = %s;"""
    cursor.execute(query, (new_age,buyer_id))
    conn.commit()
    cursor.close()
    print("✅ Buyer updated successfully!")






def delete_buyer(conn, buyer_id):
    cursor = conn.cursor()
    query = "DELETE FROM buyer.data WHERE buyer_id = %s;"
    cursor.execute(query, (buyer_id,))
    conn.commit()
    cursor.close()
    print("✅ Buyer deleted successfully!")




import json

def export_to_json(conn, filename="assignment.json"):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buyer.data;")
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
        
        insert_data(conn, "MR.1", 21, "Chocolate", "1@example.com")
        insert_data(conn, "Mr.2", 22, "Car", "2@example.com")
        insert_data(conn, "MR.3", 43, "Sport", "3@example.com")

        insert_data(conn, "MR.4", 48, "Electronic", "4@example.com")
        insert_data(conn, "MR.5", 45, "Note", "5@example.com")
        
        # Fetch and print
        name = fetch_data(conn)
        print("\n📚 Name data:", name)
        
        
        update_buyer_age(conn, 1, 48)
        
       
        delete_buyer(conn, 2)
        
        # Export to JSON
        export_to_json(conn)
        
        conn.close()