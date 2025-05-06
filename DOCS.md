# Koneksi MySQL dengan Python

## Daftar Isi

- [Koneksi MySQL dengan Python](#koneksi-mysql-dengan-python)
  - [Daftar Isi](#daftar-isi)
  - [Pendahuluan](#pendahuluan)
  - [Prasyarat](#prasyarat)
  - [Membuat Koneksi ke Database MySQL](#membuat-koneksi-ke-database-mysql)
  - [Operasi CRUD pada Database](#operasi-crud-pada-database)
    - [Create (Insert Data)](#create-insert-data)
    - [Read (Membaca Data)](#read-membaca-data)
    - [Update (Memperbarui Data)](#update-memperbarui-data)
    - [Delete (Menghapus Data)](#delete-menghapus-data)
  - [Menutup Koneksi](#menutup-koneksi)
  - [Implementasi Lengkap](#implementasi-lengkap)
  - [Penanganan Error](#penanganan-error)
  - [Tips dan Best Practices](#tips-dan-best-practices)

## Pendahuluan

Python dan MySQL adalah kombinasi yang sangat populer untuk pengembangan aplikasi berbasis data. Python menyediakan beberapa library untuk terhubung ke MySQL, dan salah satu yang paling banyak digunakan adalah `mysql-connector-python`.

## Prasyarat

Sebelum memulai, pastikan Anda telah:

1. Menginstal Python
2. Menginstal MySQL Server
3. Menginstal package mysql-connector-python:
   ```
   pip install mysql-connector-python
   ```
4. Membuat database bernama `python_basdat2025`
5. Membuat tabel `users` dengan struktur:
   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nama VARCHAR(100),
       umur INT
   );
   ```

## Membuat Koneksi ke Database MySQL

Langkah pertama adalah membuat koneksi ke database MySQL:

```python
import mysql.connector

# Membuat objek koneksi
connection = mysql.connector.connect(
    host="localhost",    # Host server MySQL
    user="root",         # Username MySQL
    password="",         # Password MySQL
    database="python_basdat2025"  # Nama database
)

# Membuat objek cursor
cursor = connection.cursor()
```

## Operasi CRUD pada Database

### Create (Insert Data)

Fungsi untuk memasukkan data ke dalam tabel:

```python
def InsertData(nama, umur):
    sqlQuery = "INSERT INTO users (nama, umur) VALUES (%s, %s)"
    value = (nama, umur)
    try:
        cursor.execute(sqlQuery, value)
        connection.commit()  # Commit perubahan ke database
        print("Data inserted successfully")
    except mysql.connector.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
```

### Read (Membaca Data)

Fungsi untuk membaca seluruh data dari tabel:

```python
def ReadData():
    sqlQuery = "SELECT * FROM users"
    try:
        cursor.execute(sqlQuery)
        result = cursor.fetchall()  # Mengambil semua baris hasil
        print(result)
    except mysql.connector.Error as error:
        print("Failed reading data from MySQL table {}".format(error))
```

### Update (Memperbarui Data)

Fungsi untuk memperbarui data berdasarkan ID:

```python
def UpdateData(id, nama, umur):
    sqlQuery = "UPDATE users SET nama=%s, umur=%s WHERE id=%s"
    value = (nama, umur, id)
    try:
        cursor.execute(sqlQuery, value)
        connection.commit()  # Commit perubahan ke database
        print("Data updated successfully")
    except mysql.connector.Error as error:
        print("Failed updating data into MySQL table {}".format(error))
```

### Delete (Menghapus Data)

Fungsi untuk menghapus data berdasarkan ID:

```python
def DeleteData(id):
    sqlQuery = "DELETE FROM users WHERE id=%s"
    value = (id,)  # Perhatikan koma untuk membuat tuple dengan satu elemen
    try:
        cursor.execute(sqlQuery, value)
        connection.commit()  # Commit perubahan ke database
        print("Data deleted successfully")
    except mysql.connector.Error as error:
        print("Failed deleting data into MySQL table {}".format(error))
```

## Menutup Koneksi

Selalu tutup cursor dan koneksi setelah selesai:

```python
def CloseConnection():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
```

## Implementasi Lengkap

```python
import mysql.connector

# Create a connection object
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_basdat2025"
)

# Create a cursor object
cursor = connection.cursor()

# Insert data into the users table
def InsertData(nama, umur):
    sqlQuery = "INSERT INTO users (nama, umur) VALUES (%s, %s)"
    value = (nama, umur)
    try:
        cursor.execute(sqlQuery, value)
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))

# Read data from the users table
def ReadData():
    sqlQuery = "SELECT * FROM users"
    try:
        cursor.execute(sqlQuery)
        result = cursor.fetchall()
        for row in result:
            print(f"ID: {row[0]}, Nama: {row[1]}, Umur: {row[2]}")
    except mysql.connector.Error as error:
        print("Failed reading data from MySQL table {}".format(error))

# Update data in the users table
def UpdateData(id, nama, umur):
    sqlQuery = "UPDATE users SET nama=%s, umur=%s WHERE id=%s"
    value = (nama, umur, id)
    try:
        cursor.execute(sqlQuery, value)
        connection.commit()
        print("Data updated successfully")
    except mysql.connector.Error as error:
        print("Failed updating data into MySQL table {}".format(error))

# Delete data from the users table
def DeleteData(id):
    sqlQuery = "DELETE FROM users WHERE id=%s"
    value = (id,)
    try:
        cursor.execute(sqlQuery, value)
        connection.commit()
        print("Data deleted successfully")
    except mysql.connector.Error as error:
        print("Failed deleting data into MySQL table {}".format(error))

# Close the connection
def CloseConnection():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

if __name__ == "__main__":
    # Contoh penggunaan:
    InsertData("Budi", 20)
    ReadData()
    UpdateData(1, "Budi", 21)
    ReadData()
    DeleteData(1)
    ReadData()
    CloseConnection()
```

## Penanganan Error

Pada kode di atas, kita menggunakan blok `try-except` untuk menangani kemungkinan error saat melakukan operasi database. Ini merupakan praktik yang baik untuk membuat program lebih robust.

## Tips dan Best Practices

1. **Gunakan Parameterized Queries**: Selalu gunakan parameter untuk query seperti `%s` untuk mencegah SQL Injection.

2. **Commit Setelah Operasi Modifikasi**: Selalu panggil `connection.commit()` setelah operasi INSERT, UPDATE, atau DELETE.

3. **Tutup Koneksi**: Selalu tutup cursor dan koneksi setelah selesai untuk membebaskan sumber daya.

4. **Gunakan with statement**: Untuk keamanan lebih, Anda bisa menggunakan `with` statement:

   ```python
   with mysql.connector.connect(...) as connection:
       with connection.cursor() as cursor:
           # operasi database
   ```

5. **Konfigurasi Koneksi Eksternal**: Pertimbangkan untuk menyimpan konfigurasi koneksi database di file konfigurasi terpisah untuk keamanan.

6. **Gunakan Connection Pooling**: Untuk aplikasi yang lebih besar, pertimbangkan untuk menggunakan
