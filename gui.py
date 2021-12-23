# import a library
from tkinter import *
import tkinter.messagebox

# create empty dictionary
mydict = {}

root = Tk() # Toplevel widget
root.geometry('400x400') # set the GUI size

# set the title
root.title("GUI to create and edit a dictionary.")

# function to add items in dictionary
def add(x, y):
    
    if x in mydict:
         print("{}:{} is already exist".format(x,y))
    else:
        mydict[x] = y
        print("{}:{} is added".format(x,y))
    
    # function to clear the content of textbox
    # which is taking input for adding pairs into dictionary
    clear1()

    
def delete(k,v):
    try:
        if mydict[k]==v:
            del mydict[k]
            print("{}:{} is deleted".format(k,v))
        else:
            error()
    except:
        error()
        
    # function to clear the content of textbox
    # which is taking input for deleting pairs from dictionary
    clear2()

# popup message
def error():
    tkinter.messagebox.showinfo("Error Message","Wrong inputs, key/value pair does not exists")
    
def clear1():
    entry_1.delete(0,"end")
    entry_2.delete(0,"end")
    
def clear2():
    entry_11.delete(0,"end")
    entry_12.delete(0,"end")

# GUI for Add -----------

# variables to get the user's input.
x = StringVar()  
y = StringVar()

# Label widget which can display text
label_1 = Label(root, text="Key" )
label_2 = Label(root, text="Value")

# Entry widget which allows displaying simple text
entry_1 = Entry(root, textvariable=x)
entry_2 = Entry(root, textvariable=y)

# Position a widget in the parent widget in a grid
label_1.grid(row=1,column=0)
label_2.grid(row=2,column=0)

entry_1.grid(row=1, column=4)
entry_2.grid(row=2, column=4)

buton= Button(root, text="Add",height=2,width=10, command=lambda :add(x.get(), y.get()))
buton.grid(row=3, column=4)

# GUI for Delete ------

# variables to get the user's input.
p = StringVar()
q = StringVar()

label_11 = Label(root, text="Key" )
label_12 = Label(root, text="Value")

entry_11 = Entry(root, textvariable=p)
entry_12 = Entry(root, textvariable=q)


label_11.grid(row=6,column=0)
label_12.grid(row=7,column=0)

entry_11.grid(row=6, column=4)
entry_12.grid(row=7, column=4)

buton = Button(root, text="Delete",height=2,width=10, command=lambda :delete(p.get(), q.get()))
buton.grid(row=8, column=4)

# print Button

buton = Button(root, text="print",height=2,width=30,command=lambda :print(mydict))
buton.grid(row=10,column=4)

root.mainloop()   # Call the mainloop of Tk.