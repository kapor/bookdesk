from tkinter import *
import backend



def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),publisher_text.get(),type_text.get(),artist_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),publisher_text.get(),type_text.get(),artist_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),publisher_text.get(),type_text.get(),artist_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),publisher_text.get(),type_text.get(),artist_text.get())

window=Tk()

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="publisher")
l4.grid(row=1,column=2)

l5=Label(window,text="type")
l5.grid(row=2,column=0)

l6=Label(window,text="artist")
l6.grid(row=2,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

publisher_text=StringVar()
e4=Entry(window,textvariable=publisher_text)
e4.grid(row=1,column=3)

type_text=StringVar()
e5=Entry(window,textvariable=type_text)
e5.grid(row=2,column=1)

artist_text=StringVar()
e6=Entry(window,textvariable=artist_text)
e6.grid(row=2,column=3)

list1=Listbox(window, height=10,width=35)
list1.grid(row=3,column=0,rowspan=6,columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# list1.bind('<<ListboxSelect>>',get_selected_row)



b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=8,column=3)

window.mainloop()
