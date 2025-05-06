import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python", # pastikkan telah membuat atau mempunyai database dengan nama python, bisa diedit sendiri
)

cursor = connection.cursor()

        
def update_data(id_user, nama_baru, umur_baru):
    sql = "UPDATE users SET nama = %s, umur = %s WHERE id = %s"
    val = (nama_baru, umur_baru, id_user)
    cursor.execute(sql, val)
    connection.commit()
    print(cursor.rowcount, "Data berhasil diupdate") 


update_data(1, "muhammad", 25)

def close_connection():
    cursor.close()
    connection.close()
