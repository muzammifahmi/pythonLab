import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python", # pastikkan telah membuat atau mempunyai database dengan nama python, bisa diedit sendiri
)

cursor = connection.cursor()

def read_data():
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)     

read_data()

# menutuos koneksi ke database
def close_connection():
    cursor.close()
    connection.close()
