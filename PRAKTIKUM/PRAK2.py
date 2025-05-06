import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python", # pastikkan telah membuat atau mempunyai database dengan nama python, bisa diedit sendiri
)

cursor = conn.cursor()

nama = input("Masukkan Nama : ")
umur = input("Masukkkan Umur : ")

sql = "INSERT INTO users (nama, umur) VALUES (%s, %s)"
val = (nama, umur)
cursor.execute(sql, val)
conn.commit()

print("Data Berhasil Disimpan")

cursor.close()
conn.close()