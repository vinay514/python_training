import mysql.connector
def insert_data(id,name,email,password):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="prathibha_cse"

    )
    print(mydb)
    mycursor=mydb.cursor()
    sql=("INSERT INTO user(id,name,email,password) VALUES (%s,%s,%s,%s)")
    val=(id,name,email,password)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record inserted.")
id=input("enter the id:")
name=input("enter the name:")
email=input("enter the email:")
password=input("enter the password:")
insert_data(id,name,email,password)