import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python", # pastikkan telah membuat atau mempunyai database dengan nama python, bisa diedit sendiri
)

cursor = connection.cursor()

# pendefisian fungsi untuk insert data ke dalam tabel
def insert_data(nama, umur):
    sql = "INSERT INTO users (nama, umur) VALUES (%s, %s)"
    val = (nama, umur) #parameter (tuple) untuk menampung data yang akan di insert
    cursor.execute(sql, val) #eksekusi query sql
    connection.commit() #menyimpan perubahan ke dalam database
    print(cursor.rowcount, "Data berhasil ditambah") #menampilkan jumlah baris dari data yang berhasil di insert

insert_data("muzammi", 30)


# menutuos koneksi ke database
def close_connection():
    cursor.close()
    connection.close()
