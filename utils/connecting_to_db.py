import mysql.connector
# Using MySQL database for python program
# 1. Creating connection to database (to make a bridge to the database)
# 2. Creating cursor (to access/enter the database)
# 3. Execute SQL Query
def connection_to_db(db:str, username:str, password:str):
    """Connect to MySQL Database
    """
    try:
        print("Log in")
        username = input("Enter username: ") #insert mysql username
        password = input("Enter password: ") #insert mysql password
        if username == "root" and password == "19Mei1995":
            conn = mysql.connector.connect(host="localhost",
                                           user=username,
                                           password=password,
                                           database=db)
            print("Connected to database")
            return conn
        else:
            print("Invalid input")
            exit()
    except Exception as e:
        print(f"Error connecting to database: {e}")


def exec_query(conn:object, query:str):
    """Executing query

    Args:
        conn (object): MySQL Connector
        query (str): Query

    Returns:
        _type_: _description_
    """
    # Creating access to database
    mycursor = conn.cursor()

    # Execute query
    mycursor.execute(query)

    # Fetch data
    return mycursor.fetchall(), mycursor.column_names

conn = connection_to_db("ophthalmology_patients","root","19Mei1995")