from tkinter import *
from tkinter import ttk

def ConvertedLength():
    Amount_ = int(_Amount.get())
    if x.get() == "":
        _ConvertedAmount.config(text="Choose\nAmount")
    elif x.get() == "Kilometers":
        _ConvertedAmount.config(text=f"Converted Amount:\n{Amount_ * 0.001}km")
    elif x.get() == "Centimeters":
        _ConvertedAmount.config(text=f"Converted Amount:\n{Amount_ * 100}cm")
    elif x.get() == "Inches":
        _ConvertedAmount.config(text=f"Converted Amount:\n{Amount_ * 39.3701}inch")
    elif x.get() == "Feet":
        _ConvertedAmount.config(text=f"Converted Amount:\n{Amount_ * 3.28084}ft")
    elif x.get() == "Kilograms":
        _ConvertedAmount.config(text=f"Converted Amount:\n{Amount_ * 0.001}kg")
    elif x.get() == "Ounce":
        _ConvertedAmount.config(text=f"Converted Amount:\n{Amount_ * 0.00220462}oz")
    elif x.get() == "Pounds":
        _ConvertedAmount.config(text=f"Converted Amount:\n{Amount_ * 0.035274}lb")
    else:
        print()



window = Tk()
window.title("Converter Application")
window.geometry("195x230")


x = StringVar()  #To Put Value On The List

Text1 = Label(master=window,
              text="Meters/Grams",
              font=("Arial",12,"bold"))
Text1.grid(row=0,column=0,padx=5,pady=5)

#Amount To Convert Input
_Amount = Entry(master=window,
                font=("Arial",12,"bold"),
                width=15)
_Amount.grid(row=1,column=0,padx=5,pady=5)

#Option Menus (Dropdown)
_DropdownLength = ttk.Combobox(master=window,
                         values=["Kilometers","Centimeters","Inches","Feet","Kilograms","Ounce","Pounds"],
                         textvariable=x)
_DropdownLength.grid(row=2,column=0,padx=5,pady=5)

#Converted Length Output
_ConvertedAmount = Label(master=window,
                         text="Converted Amount: ",
                         font=("Arial",12,"bold"))
_ConvertedAmount.grid(row=4,column=0,padx=5,pady=5)

#Button Converter
_ConvertButton = Button(master=window,
                       text="Convert",
                       font=("Arial",12,"bold"),
                       command=ConvertedLength)
_ConvertButton.grid(row=3,column=0,padx=5,pady=5)


window.mainloop()