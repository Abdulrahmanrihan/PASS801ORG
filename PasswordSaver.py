from tkinter import *
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
import sqlite3

root = Tk()
root.title('Password Saver')
root.iconbitmap('images.ico')
root.geometry('360x580')
root.configure(bg="snow")

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
        print_data += str(record[0]) + ' \n ' + str(record[1]) + ' \n ' + str(record[2]) + '\n\n'
        
    query_table = ScrolledText(master=root, width=35, bg="snow")
    query_table.grid(row=6,column=0, columnspan=2, pady =20)
    query_table.insert(INSERT, print_data)
    
    conn. commit()
    conn.close()

#title
title = Label(root, text = "PASS801ORG", font=('Impact', 40), bg="snow")
title.grid(row=0, column=0, columnspan=2, padx=10)

#create Entries
website_name = Entry(root, width=30)
website_name.grid(row=1, column=1, padx=20, pady=5)
username = Entry(root, width=30)
username.grid(row=2, column=1, padx=20, pady=5)
password = Entry(root, width=30)
password.grid(row=3, column=1, padx=20, pady=5)

#create labels
website_name_label = Label(root, text="Website name", bg="snow")
website_name_label.grid(row=1, column=0, padx=20, pady=10)
username_label = Label(root, text="username", bg="snow")
username_label.grid(row=2, column=0, padx=20, pady=5)
password_label = Label(root, text="password", bg="snow")
password_label.grid(row=3, column=0, padx=20, pady=5)

submit = Button(root, text= "Add to database", command= submitData, width=42)
submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

databasebtn = Button(root, text= "Show database", command= query, width=42)
databasebtn.grid(row=5, column=0, columnspan=2, padx=10, pady=0)

conn. commit()
conn.close()

root.mainloop()
