import mysql.connector
def update(name,id):

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="prathibha_cse"

        )
    print(mydb)
    mycursor=mydb.cursor()
    sql="update user set name=riya where id=%s"
    val=(id)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
name=input("enter name:")
id=input("enter id")
update(name,id)

