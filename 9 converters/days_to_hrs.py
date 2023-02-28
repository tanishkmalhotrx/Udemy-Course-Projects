from tkinter import *

window = Tk()

def days_to_hrs():
    print(e1_value.get())
    hrs = float(e1_value.get()) * 24
    t1.insert(END, hrs)

b1 = Button(window,text="Convert", command=days_to_hrs)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()