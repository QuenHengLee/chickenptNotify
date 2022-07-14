# Importing module
import mysql.connector
 
# Creating connection object
connect_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "chickenpt"
)

# Printing the connection object
print(connect_db)