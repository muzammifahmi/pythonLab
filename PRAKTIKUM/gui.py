import mysql.connector
import tkinter as tk
from tkinter import messagebox

def save_data():
    nama = entry_nama.get()
    umur = entry_umur.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python", # pastikkan telah membuat atau mempunyai database dengan nama python, bisa diedit sendiri
    )

    cursor = conn.cursor()

    sql = "INSERT INTO users (nama, umur) VALUES (%s, %s)"
    val = (nama, umur)
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Data saved successfully!")
    cursor.close()
    conn.close()

root = tk.Tk()
root.title("Data Entry Form")
root.geometry("300x200")

tk.Label(root, text="Nama : ").pack()
entry_nama = tk.Entry(root, width=30)
entry_nama.pack()

tk.Label(root, text="Umur : ").pack()
entry_umur = tk.Entry(root, width=30)
entry_umur.pack()

tk.Button(root, text="Save", command=save_data).pack()

root.mainloop()