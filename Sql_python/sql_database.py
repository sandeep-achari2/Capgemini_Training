# Python implementation to create a Database in MySQL
import mysql.connector

# Connecting to the MySQL server
def connection_to_sql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="sandeep"
        )
        print("Database connected")
        return connection
    except mysql.connector.Error as e:  # Corrected Exception Handling
        print("Error while connecting to MySQL:", e)
        return None

# Function to create a table
def create_table(connection):
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        query = "CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name VARCHAR(50), age INT, gender CHAR(10))"
        cursor.execute(query)
        print("Table created successfully")
    except mysql.connector.Error as e:
        print("Error while creating table:", e)
    finally:
        cursor.close()

# Function to insert values
def insert_values(connection):
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "INSERT INTO students (id, name, age, gender) VALUES (%s, %s, %s, %s)"
        values = [
            (1, 'sandeep', 21, 'male'),
            (2, 'harish', 23, 'male'),
            (3, 'vasantha', 20, 'female')
        ]
        cursor.executemany(query, values)
        connection.commit()
        print("Values inserted successfully")
    except mysql.connector.Error as e:
        print("Error while inserting values:", e)
    finally:
        cursor.close()

# Function to update values
def update_query(connection):
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        query = "UPDATE students SET age=23 WHERE name='sandeep'"
        cursor.execute(query)
        connection.commit()
        print("Values updated successfully")
    except mysql.connector.Error as e:
        print("Error while updating values:", e)
    finally:
        cursor.close()

# Function to delete values
def delete_query(connection):
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        query = 'DELETE FROM students WHERE name="sandeep"'
        cursor.execute(query)
        connection.commit()
        print("Delete operation successful")
    except mysql.connector.Error as e:
        print("Error while deleting values:", e)
    finally:
        cursor.close()

# Function to drop the table
def drop_table(connection):
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        query = "DROP TABLE IF EXISTS students"
        cursor.execute(query)
        print("Table dropped successfully")
    except mysql.connector.Error as e:
        print("Error while dropping table:", e)
    finally:
        cursor.close()

# Main function
def main():
    connection = connection_to_sql()  # Open a single connection
    
    if connection:
        create_table(connection)
        insert_values(connection)
        update_query(connection)
        delete_query(connection)
        drop_table(connection)
        
        connection.close()  # Close the connection after all operations
        print("Database connection closed.")

main()
