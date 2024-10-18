import mysql.connector

# Establish connection to MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',  # Your MySQL username
    password='your_password',  # Your MySQL password
    database='sneaker_db',  # Your database name
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Define the SQL query to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS sneakers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    size INT,
    price DECIMAL(10, 2),
    stock INT
);
'''

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# Commit the transaction
db_connection.commit()

# Close the cursor and connection
cursor.close()
db_connection.close()

print("Table created successfully!")
