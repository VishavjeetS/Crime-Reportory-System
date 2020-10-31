from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql


def insert():
    name_label=e_name_label.get()
    lastname_label=e_lastname_label.get()
    phone_label=e_phone_label.get()
    location_label=e_location_label.get()

    if(name_label=="" or lastname_label=="" or phone_label=="" or location_label==""):
        Messagebox.showinfo("All fields are Required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.excute("insert into Report values('"+ name_label +"','"+lastname_label +"','"+ phone +"','"+location_label +"')")
        cursor.execute("commit");
        Messagebox.showinfo("Insert Status","Inserted Succesfull");
        con.close();

root = Tk()
root.geometry("600x400")
root.title("Crime Reporting ")

name_label=Label(root,text="First Name",font=('bold', 10))
name_label.place(x=20,y=30)

lastname_label=Label(root,text="Last Name",font=('bold', 10))
lastname_label.place(x=20,y=60)

phone_label=Label(root,text="Phone Number",font=('bold', 10))
phone_label.place(x=20,y=90)

location_label=Label(root,text="Crime Location",font=('bold', 10))
location_label.place(x=20,y=120)

# Entry

e_name_label=Entry()
e_name_label.place(x=150,y=30)

e_lastname_label=Entry()
e_lastname_label.place(x=150,y=60)

e_phone_label=Entry()
e_phone_label.place(x=150,y=90)

e_location_label=Entry()
e_location_label.place(x=150,y=120)

# Button

insert  = Button(root, text="Submit", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

# delete = Button(root, text="delete", font=("italic", 10), bg="white", command=delete)
# delete.place(x=70, y=140)

# update  = Button(root, text="update", font=("italic", 10), bg="white", command=update)
# update.place(x=130, y=140)

# get  = Button(root, text="get", font=("italic", 10), bg="white", command=get)
# get.place(x=190, y=140)


# ButtonList = Button(root, text='View Complain', font=("bold", 10),bg="teal")
# ButtonList.place(x=80, y=300)

# ButtonSubmit = Button(root, text='Submit Now', font=("bold", 10),bg="orange")
# ButtonSubmit.place(x=300, y=300)



root.mainloop()