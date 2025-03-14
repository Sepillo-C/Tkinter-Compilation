from tkinter import *

def notes():
    n1 = _Entry1.get()
    print(n1)

window = Tk()

_Addbutton = Button(window,
                    text="Add",
                    command=notes,
                    background="#505A5B",
                    foreground="#F5F1E3",
                    activebackground="#505A5B",
                    activeforeground="#F5F1E3")
_Addbutton.place(x=60,y=60)


_Entry1 = Entry(window,
                font=("Arial", 30),
                width=10,
                background="#505A5B",
                foreground="#F5F1E3"
               )
_Entry1.place(x=60,y=8)

#Window Configurations
window.title("Notepad Application")
window.config(background="#343F3E")
window.geometry("350x500")
window.mainloop()