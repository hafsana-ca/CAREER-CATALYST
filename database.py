import mysql.connector

def select(query):
    try:
        con = mysql.connector.connect(
            user="root",
            password="new_password",  # Replace with your MySQL root password
            host="localhost",
            database="know_it_right",  # Replace with your database name
            port=3306
        )
        cursor = con.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        con.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert(query):
    try:
        con = mysql.connector.connect(
            user="root",
            password="new_password",
            host="localhost",
            database="know_it_right",
            port=3306
        )
        cursor = con.cursor(dictionary=True)
        cursor.execute(query)
        con.commit()
        result = cursor.lastrowid
        cursor.close()
        con.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def update(query):
    try:
        con = mysql.connector.connect(
            user="root",
            password="new_password",
            host="localhost",
            database="know_it_right",
            port=3306
        )
        cursor = con.cursor(dictionary=True)
        cursor.execute(query)
        con.commit()
        result = cursor.rowcount
        cursor.close()
        con.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def delete(query):
    try:
        con = mysql.connector.connect(
            user="root",
            password="new_password",
            host="localhost",
            database="know_it_right",
            port=3306
        )
        cursor = con.cursor(dictionary=True)
        cursor.execute(query)
        con.commit()
        result = cursor.rowcount
        cursor.close()
        con.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
