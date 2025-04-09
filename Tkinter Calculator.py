from tkinter import *

#Function for addition
def Add():
    a = int(_Val1.get())
    b = int(_Val2.get())
    
    _Total.config(text=f"Total: {a + b}")

#Function for subtraction
def Sub():
    a = int(_Val1.get())
    b = int(_Val2.get())
    
    _Total.config(text=f"Total: {a - b}")

#Function for multiplication
def Mult():
    a = int(_Val1.get())
    b = int(_Val2.get())
    
    _Total.config(text=f"Total: {a * b}")

#Function for division
def Div():
    a = int(_Val1.get())
    b = int(_Val2.get())
    
    if a == 0 or b == 0:
        Invalid = Toplevel()
        Invalid.title("Invalid Amount")
        Invalid.geometry("250x100")

        LabelInvalid = Label(Invalid,
                             text="Invalid amount, please enter a proper amount",)

        LabelInvalid.grid(row=0,
                          column=0,
                          columnspan=3,
                          pady=2)

        ButtonInvalid = Button(Invalid,
                               text="Close",
                               command=Invalid.destroy)
        ButtonInvalid.grid(row=1,
                           column=1,
                           pady=2)
    else:
        result = a / b
        _Total.config(text=f"Total: {result:.2f}")


#Mainwindow
window = Tk()

window.title("Bootleg Calculator")
window.geometry("275x110")

_TVal1 = Label(window,
               text = "Value 1")
_TVal1.grid(row=0,
            column=0,
            pady=2,
            padx=2)

_Val1 = Entry(window)
_Val1.grid(row=0,
           column=1,
           columnspan=5,
           pady=2,
           padx=2)


_TVal2 = Label(window,
               text = "Value 2")
_TVal2.grid(row=1,
            column=0,
            pady=2,
            padx=2)
_Val2 = Entry(window)
_Val2.grid(row=1,
           column=1,
           columnspan=5,
           pady=2,
           padx=2)

_Total = Label(window,
               text="Total:")
_Total.grid(row=3,
            column=0,
            pady=2,
            padx=2)

#Addition Button
AdditionLogo = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter-Compilation\\Calculator Logo\\AdditionLogo.png')
AddResize = AdditionLogo.subsample(20,20)

_AdditionButton = Button(window,
                         image=AddResize,
                         command=Add)
_AdditionButton.grid(row=4,
                     column=1,
                     pady=2,
                     padx=2)

#Subtraction Button
SubtractionLogo = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter-Compilation\\Calculator Logo\\SubtractionLogo.png')
SubResize = SubtractionLogo.subsample(20,20)

_SubtractionButton = Button(window,
                            image=SubResize,
                            command=Sub)
_SubtractionButton.grid(row=4,
                        column=2,
                        pady=2,
                        padx=2)

#Multiplication Button
MultiplicationLogo = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter-Compilation\\Calculator Logo\\MultiplicationLogo.png')
MultResize = MultiplicationLogo.subsample(20,20)

_MultiplicationButton = Button(window,
                               image=MultResize,
                               command=Mult)
                                                  
_MultiplicationButton.grid(row=4, 
                           column=3,
                           pady=2,
                           padx=2)
                                              
#Division Button                                              
DivisionLogo = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter-Compilation\\Calculator Logo\\DivisionLogo.png')
DivResize = DivisionLogo.subsample(20,20)

_DivisionLogo = Button(window,
                       image=DivResize,
                       command=Div)
                        
_DivisionLogo.grid(row=4,
                   column=4,
                   pady=2,
                   padx=2)
                    
window.mainloop()