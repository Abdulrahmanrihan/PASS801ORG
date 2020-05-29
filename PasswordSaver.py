from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Password Saver')
root.iconbitmap('C:/Users/Abdelrahman Hesham/Desktop/PythonTkinter/images.ico')
root.geometry('360x220')

#database

conn = sqlite3.connect('passwordsDatabase.db')

#create cursor
c = conn.cursor()
'''
c.execute("""CREATE TABLE passwords (
            website_name text,
            username text,
            password text
                )""")
'''
# submit data to database function
def submitData():
    conn = sqlite3.connect('passwordsDatabase.db')
    c = conn.cursor()

    c.execute("INSERT INTO passwords VALUES(:website_name, :username, :password)",
              {
                  'website_name' : website_name.get(),
                  'username' : username.get(),
                  'password' : password.get(), }
              )
    conn. commit()
    conn.close()
    
    website_name.delete(0, END)
    username.delete(0, END)
    password.delete(0, END)

#create query function
def query():
    conn = sqlite3.connect('passwordsDatabase.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM passwords")
    data = c.fetchall()
    print(data)

    print_data=''
    for record in data:
        print_data += str(record) + '\n'
        
    query_table = Label(root, text=print_data)
    query_table.grid(row=5,column=0, columnspan=2)
    
    conn. commit()
    conn.close()
#create Entries
website_name = Entry(root, width=30)
website_name.grid(row=0, column=1, padx=20, pady=5)
username = Entry(root, width=30)
username.grid(row=1, column=1, padx=20, pady=5)
password = Entry(root, width=30)
password.grid(row=2, column=1, padx=20, pady=5)

#create labels
website_name_label = Label(root, text="Website name")
website_name_label.grid(row=0, column=0, padx=20, pady=10)
username_label = Label(root, text="username")
username_label.grid(row=1, column=0, padx=20, pady=5)
password_label = Label(root, text="password")
password_label.grid(row=2, column=0, padx=20, pady=5)

submit = Button(root, text= "Add to database", command= submitData, width=42)
submit.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

databasebtn = Button(root, text= "Show database", command= query, width=42)
databasebtn.grid(row=4, column=0, columnspan=2, padx=10, pady=0)

conn. commit()
conn.close()

root.mainloop()
