from tkinter import *
import be



def view_command():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)

# search(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get(),quality_text.get(),price_text.get(),location_text.get(),genre_text.get(),weight_text.get(),pages_text.get(),isbn_text.get(),description_text.get(),notes_text.get()

def search_command():
    list1.delete(0,END)
    for row in be.search(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get(),quality_text.get(),price_text.get(),location_text.get(),genre_text.get(),weight_text.get(),pages_text.get(),isbn_text.get(),description_text.get(),image_text.get(),notes_text.get()):
        list1.insert(END,row)

def add_command():
    be.insert(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get(),quality_text.get(),price_text.get(),location_text.get(),genre_text.get(),weight_text.get(),pages_text.get(),isbn_text.get(),description_text.get(),image_text.get(),notes_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get(),quality_text.get(),price_text.get(),location_text.get(),genre_text.get(),weight_text.get(),pages_text.get(),isbn_text.get(),description_text.get(),image_text.get(),notes_text.get()))

def delete_command():
    list1.delete(0,END)

def update_command():
    list1.delete(0,END)


window=Tk()

window.wm_title("Bookdesk")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.insert(0, "")
e1.grid(row=0,column=1)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.insert(0, "")
e2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=0,column=4)
year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.insert(0, "")
e3.grid(row=0,column=5)

l4=Label(window,text="Type")
l4.grid(row=1,column=0)
type_text=StringVar()
e4=Entry(window,textvariable=type_text)
e4.insert(0, "")
e4.grid(row=1,column=1)

l5=Label(window,text="Publisher")
l5.grid(row=1,column=2)
publisher_text=StringVar()
e5=Entry(window,textvariable=publisher_text)
e5.insert(0, "")
e5.grid(row=1,column=3)

l6=Label(window,text="Artist")
l6.grid(row=1,column=4)
artist_text=StringVar()
e6=Entry(window,textvariable=artist_text)
e6.insert(0, "")
e6.grid(row=1,column=5)

l7=Label(window,text="Quality")
l7.grid(row=2,column=0)
quality_text=StringVar()
e7=Entry(window,textvariable=quality_text)
e7.insert(0, "")
e7.grid(row=2,column=1)

l8=Label(window,text="Price")
l8.grid(row=2,column=2)
price_text=StringVar()
e8=Entry(window,textvariable=price_text)
e8.insert(0, "")
e8.grid(row=2,column=3)

l9=Label(window,text="Location")
l9.grid(row=2,column=4)
location_text=StringVar()
e9=Entry(window,textvariable=location_text)
e9.insert(0, "")
e9.grid(row=2,column=5)

l10=Label(window,text="Genre")
l10.grid(row=3,column=0)
genre_text=StringVar()
e10=Entry(window,textvariable=genre_text)
e10.insert(0, "")
e10.grid(row=3,column=1)

l11=Label(window,text="Weight")
l11.grid(row=3,column=2)
weight_text=StringVar()
e11=Entry(window,textvariable=weight_text)
e11.insert(0, "")
e11.grid(row=3,column=3)

l12=Label(window,text="Pages")
l12.grid(row=3,column=4)
pages_text=StringVar()
e12=Entry(window,textvariable=pages_text)
e12.insert(0, "")
e12.grid(row=3,column=5)

l13=Label(window,text="ISBN")
l13.grid(row=4,column=0)
isbn_text=StringVar()
e13=Entry(window,textvariable=isbn_text)
e13.insert(0, "")
e13.grid(row=4,column=1)

l14=Label(window,text="Description")
l14.grid(row=4,column=2)
description_text=StringVar()
e14=Entry(window,textvariable=description_text)
e14.insert(0, "")
e14.grid(row=4,column=3)

l15=Label(window,text="Image")
l15.grid(row=4,column=4)
image_text=StringVar()
e15=Entry(window,textvariable=image_text)
e15.insert(0, "0")
e15.grid(row=4,column=5)

l16=Label(window,text="Notes")
l16.grid(row=5,column=0)
notes_text=StringVar()
e16=Entry(window,textvariable=notes_text)
e16.insert(0, "")
e16.grid(row=5,column=1,rowspan=1,columnspan=5,sticky="EW")









list1=Listbox(window, height=10, width=60)
list1.grid(row=6,column=0,rowspan=6,columnspan=5,sticky="W")

sb1=Scrollbar(window)
sb1.grid(row=6,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)





b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=6,column=5)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=7,column=5)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=8,column=5)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=9,column=5)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=10,column=5)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=11,column=5)

window.mainloop()
