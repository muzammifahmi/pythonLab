import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python", # pastikkan telah membuat atau mempunyai database dengan nama python, bisa diedit sendiri
)

cursor = connection.cursor()
    
def delete_data(id_user):
    sql = "DELETE FROM users WHERE id = %s"
    val = (id_user,)
    cursor.execute(sql, val)
    connection.commit()
    print(cursor.rowcount, "Data berhasil dihapus")


delete_data(1) # menghapus data menurut id


# menutuos koneksi ke database
def close_connection():
    cursor.close()
    connection.close()
