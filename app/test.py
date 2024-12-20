import tkinter as tk

# if you get an error saying the method is not defined... place "tk." in front of it

window = tk.Tk()

def km_to_m():
	# equation to get distance
	miles=float(e1_value.get())*1.6
	# use the insert method to define the placement
	t1.insert(tk.END, miles)

b1=tk.Button(window, text="Click me!", command=km_to_m)
# b1=tk.Button(window, text="Click me!", command=lambda: print("Button clicked!"))
b1.grid(row=3,column=1)

e1_value=tk.StringVar()
e1=tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1=tk.Text(window, height=1, width=20)
t1.grid(row=2, column=1)

window.mainloop()
