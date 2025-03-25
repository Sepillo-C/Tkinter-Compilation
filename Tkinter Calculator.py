from tkinter import *

CurOpperation = None

def Add_Operation():
    global CurOpperation
    CurOpperation = "add"

def Submit():
    a = int(_Val1.get())
    b = int(_Val2.get())
    
    _Total.config(text=f"Total: {addition}")



window = Tk()

_TVal1 = Label(window,
               text = "Value 1")
_TVal1.grid(row=0,
            column=0,
            pady=2,)

_Val1 = Entry(window)
_Val1.grid(row=0,
           column=1,
           pady=2)


_TVal2 = Label(window,
               text = "Value 2")
_TVal2.grid(row=1,
            column=0,
            pady=2,)
_Val2 = Entry(window)
_Val2.grid(row=1,
           column=1,
           pady=2)

_Total = Label(window,
               text="Total:")
_Total.grid(row=3,
            column=0,
            pady=2)

_SubmitButton = Button(window,
                       text="Submit",
                       command=Submit)
_SubmitButton.grid(row=4,
                   column=0,
                   pady=2)

window.mainloop()