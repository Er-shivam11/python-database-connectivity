import mysql.connector

# Database connection details
db_config = {
    'host': 'localhost',
    'database': 'etot',
    'user': 'root',
    'password': ''
}

# Connect to the database
mydb = mysql.connector.connect(
    host=db_config['host'],
    database=db_config['database'],
    user=db_config['user'],
    password=db_config['password']
)

cursor = mydb.cursor()

# Show existing tables
cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)