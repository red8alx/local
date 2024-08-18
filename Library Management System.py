import mysql.connector

# Database connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="library_management_system"
)

mycursor = mydb.cursor()
print("Connection Established...")

#Insert Function
def insertToTable(title, author, ISBN):
    sql = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
    val = (title, author, ISBN)
    mycursor.execute(sql, val)
    mydb.commit()
#Search Function
def searchTable(title, author):
    sql = "select * from books where title = %s"
    val = (title,)
    
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    
    print(f"A book by: {author}")
    for row in myresult:
        print(row)
    
#Listing Function
def listAll():
    sql = "select * from books;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("List of All Books:...")
    for row in myresult:
        print(row)

#Delete Function
def deleteBook(id):
    sql = "delete from books where id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()

#Calling the functions...
deleteBook(1)
insertToTable("Python made easy", "Bob Alice", "676-xyz-2234")
searchTable("C++ Primer", "Rediet A.")
listAll()

# Close connections
mycursor.close()
mydb.close()

print("Database connection closed.")