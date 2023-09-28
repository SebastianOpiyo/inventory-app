import cx_Oracle

def create_connection():
    try:
        conn = cx_Oracle.connect("username/password@localhost/xe")  # Replace with your Oracle connection details
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        return None
