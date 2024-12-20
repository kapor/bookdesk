from tkinter import *
import be


def view_btn():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)

# def search_btn():
#     list1.delete(0,END)
#     for row in be.search(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get(),quality_text.get(),price_text.get(),location_text.get(),genre_text.get(),weight_text.get(),pages_text.get(),isbn_text.get(),desc_text.get(),image_text.get(),notes_text.get()):
#         list1.insert(END,row)

def search_btn():
    list1.delete(0,END)
    for row in be.search(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get()):
        list1.insert(END,row)


# def add_btn():
# 	be.insert(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get(),quality_text.get(),price_text.get(),location_text.get(),genre_text.get(),weight_text.get(),pages_text.get(),isbn_text.get(),desc_text.get(),image_text.get(),notes_text.get())



def add_btn():
    be.insert(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),type_text.get(),publisher_text.get(),artist_text.get()))


def update_btn():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)

def delete_btn():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)

def close_btn():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)




window=Tk()


l1=Label(window, text="Title")
l1.grid(row=0, column=0)
title_text=StringVar()
e1=Entry(window,textvariable="title_text")
e1.grid(row=0,column=1)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)
author_text=StringVar()
e2=Entry(window,textvariable="author_text")
e2.grid(row=0,column=3)

l3=Label(window, text="Year")
l3.grid(row=0, column=4)
year_text=StringVar()
e3=Entry(window,textvariable="year_text")
e3.grid(row=0,column=5)

l4=Label(window, text="Type")
l4.grid(row=1, column=0)
type_text=StringVar()
e4=Entry(window,textvariable="type_text")
e4.grid(row=1,column=1)

l5=Label(window, text="Publisher")
l5.grid(row=1, column=2)
publisher_text=StringVar()
e5=Entry(window,textvariable="publisher_text")
e5.grid(row=1,column=3)

l6=Label(window, text="Artist")
l6.grid(row=1, column=4)
artist_text=StringVar()
e6=Entry(window,textvariable="artist_text")
e6.grid(row=1,column=5)

# l7=Label(window, text="Quality")
# l7.grid(row=3, column=0)
# quality_text=StringVar()
# e7=Entry(window, textvariable="quality_text")
# e7.grid(row=3, column=1)

# l8=Label(window, text="Price")
# l8.grid(row=3, column=2)
# price_text=StringVar()
# e8=Entry(window, textvariable="price_text")
# e8.grid(row=3, column=3)

# l9=Label(window, text="Location")
# l9.grid(row=3, column=4)
# location_text=StringVar()
# e9=Entry(window, textvariable="location_text")
# e9.grid(row=3, column=5)

# l10=Label(window, text="Genre")
# l10.grid(row=4, column=0)
# genre_text=StringVar()
# e10=Entry(window, textvariable="genre_text")
# e10.grid(row=4, column=1)

# l11=Label(window, text="Weight")
# l11.grid(row=4, column=2)
# weight_text=StringVar()
# e11=Entry(window, textvariable="weight_text")
# e11.grid(row=4, column=3)

# l12=Label(window, text="Pages")
# l12.grid(row=4, column=4)
# pages_text=StringVar()
# e12=Entry(window, textvariable="pages_text")
# e12.grid(row=4, column=5)

# l13=Label(window, text="ISBN")
# l13.grid(row=5, column=0)
# isbn_text=StringVar()
# e13=Entry(window, textvariable="isbn_text")
# e13.grid(row=5, column=1)

# l14=Label(window, text="Description")
# l14.grid(row=5, column=2)
# desc_text=StringVar()
# e14=Entry(window, textvariable="desc_text")
# e14.grid(row=5, column=3)

# l15=Label(window, text="Image")
# l15.grid(row=5, column=4)
# image_text=StringVar()
# e15=Entry(window, textvariable="image_text")
# e15.grid(row=5, column=5)

# l16=Label(window, text="Notes")
# l16.grid(row=2, column=2)
# notes_text=StringVar()
# e16=Entry(window, textvariable="notes_text")
# e16.grid(row=2, column=3)

list1=Listbox(window, height=10,width=80)
list1.grid(row=7, column=0, rowspan=6, columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=7, column=5, rowspan=6)
sb1.tkraise()

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


b1=Button(window, text="View all", width=12, height=0, command=view_btn)
b1.grid(row=7, column=6)

b2=Button(window, text="Search", width=12, height=0, command=search_btn)
b2.grid(row=8, column=6)

b3=Button(window, text="Add", width=12, height=0, command=add_btn)
b3.grid(row=9, column=6)

b4=Button(window, text="Update", width=12, height=0, command=update_btn)
b4.grid(row=10, column=6)

b5=Button(window, text="Delete", width=12, height=0, command=delete_btn)
b5.grid(row=11, column=6)

b6=Button(window, text="Close", width=12, height=0, command=close_btn)
b6.grid(row=12, column=6)




window.mainloop()