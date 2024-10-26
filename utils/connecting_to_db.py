import mysql.connector
def connection_to_db(db:str, username:str, password:str):
    """Connect to MySQL Database
    """
    try:
        if username == "root" and password == "19Mei1995":  #username and password can be adjusted to match your mysql username and password
            conn = mysql.connector.connect(host="localhost",
                                           user=username,
                                           password=password,
                                           database=db)
            print("\nConnected to database")
            return conn
        else:
            print("\nInvalid input")
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

print("Log in")
username = input("Enter username: ") #insert mysql username
password = input("Enter password: ") #insert mysql password
conn = connection_to_db("ophthalmology_patients",username,password)