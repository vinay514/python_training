import mysql.connector
mybd=mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="vinay_ece"
)
print("connected database successfully.")