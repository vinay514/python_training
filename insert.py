import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
name=input("enter your name:")
age=int(input("enter your age:"))
cursor.execute("INSERT INTO users(name,age) VALUES(?,?)",(name,age))
conn.commit()
conn.close()