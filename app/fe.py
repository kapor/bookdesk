from tkinter import *
import be


def view_btn():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)

window=Tk()


l1=Label(window, text="Title")
l1.grid(row=0, column=0)
title_text=StringVar()
e1=Entry(window, textvariable="title_text")
e1.grid(row=0, column=1)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)
author_text=StringVar()
e2=Entry(window, textvariable="author_text")
e2.grid(row=0, column=3)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)
year_text=StringVar()
e3=Entry(window, textvariable="year_text")
e3.grid(row=1, column=1)

l4=Label(window, text="Type")
l4.grid(row=1, column=2)
type_text=StringVar()
type_text.set('one') #default value
d4=OptionMenu(window, type_text, "one", "two", "three")
d4.grid(row=1, column=3, sticky='nsew')

l5=Label(window, text="Genre")
l5.grid(row=2, column=0)
genre_text=StringVar()
e5=Entry(window, textvariable="genre_text")
e5.grid(row=2, column=1)

l6=Label(window, text="ISBN")
l6.grid(row=2, column=2)
isbn_text=StringVar()
e6=Entry(window, textvariable="isbn_text")
e6.grid(row=2, column=3)

list1=Listbox(window, height=18,width=54)
list1.grid(row=3, column=0, rowspan=6, columnspan=4)

sb1=Scrollbar(window)
sb1.grid(row=3,column=4)
sb1.tkraise()

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


b1=Button(window, text="View all", width=12, height=2, command=view_btn)
b1.grid(row=3, column=6)

b2=Button(window, text="Search entry", width=12, height=2)
b2.grid(row=4, column=6)

b3=Button(window, text="Add entry", width=12, height=2)
b3.grid(row=5, column=6)

b4=Button(window, text="Update", width=12, height=2)
b4.grid(row=6, column=6)

b5=Button(window, text="Delete", width=12, height=2)
b5.grid(row=7, column=6)

b6=Button(window, text="Close", width=12, height=2)
b6.grid(row=8, column=6)





window.mainloop()