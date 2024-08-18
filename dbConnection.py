import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'pass',
    database = 'inventory'
)
mycursor = mydb.cursor()

#SELECT Retrieve data from a table
"""mycursor.execute('select * from products')
resultSet = mycursor.fetchone()
for i in resultSet:
    print(i)"""

#INSERT Insert new data into a table
sql = "insert into products values (%s, %s, %s)"
val = (11,'Bluetooth', 32)
mycursor.execute(sql, val)
mydb.commit()

#UPDATE Modify existing data in a table
"""sql = "update products set productName = %s where productID = %s"
val = ("Flash Drive --updated", 1)
mycursor.execute(sql, val)
mydb.commit()"""

#DELETE Remove data from a table
#sql = "delete from products where productID = 5"
"""sql = "delete from products where productID = %s"
val = (4,)
mycursor.execute(sql, val)
mydb.commit()"""

# Close the connection to the database using mycursor.close() and mydb.close() when you’re finished.
mycursor.close()
mydb.close()
print("Database connection closed.")