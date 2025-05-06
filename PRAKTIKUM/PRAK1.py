import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python", # pastikkan telah membuat atau mempunyai database dengan nama python, bisa diedit sendiri
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()
for row in rows:
    print("ID: ", row[0])
    print("Nama: ", row[1])
    print("Umur: ", row[2])
    print("-"*20)
    
cursor.close()
conn.close()