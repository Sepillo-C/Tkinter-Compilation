from tkinter import *
from tkinter import ttk

def Center_Window(win, width=500, height=300):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 5) - (height // 5)
    
    win.geometry(f"{width}x{height}+{x}+{y}")

#Error For No Value
def ErrorNoValue():
    ErrorTop = Toplevel()
    Center_Window(ErrorTop, width=70, height=100)

    SelectError = Label(master=ErrorTop,
                        text="Select A Unit\nTo Convert",
                        font=("Arial", 12, "bold"))
    SelectError.grid(row=1, column=0, padx=5, pady=5)

    SelectError1 = Button(master=ErrorTop,
                          text="Close",
                          command=ErrorTop.destroy)
    SelectError1.grid(row=2, column=0, padx=5, pady=5)


# Conversion Meters
def ConvertFromMeters(amount, to_unit):
    ConversionFactor = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Grams": None,  # Grams is for mass.
        "Kilograms": None,  #Kilograms is for mass.
        "Ounce": None,  # Ounce is mass.
        "Pounds": None  # Pounds is mass.
    }
    
    if to_unit in ConversionFactor and ConversionFactor[to_unit] is not None:
        return amount * ConversionFactor[to_unit]
    else:
        return None

def Converted():
    Input_Val = _Amount.get()

    if Input_Val == "":
        ErrorNoValue()
        return
    try:
        Amount_ = float(Input_Val)
    except ValueError:
        _ConvertedAmount.config(text="Invalid Input.\nPlease Enter A Number")
        return

    From_Unit = ToConvertVar.get()
    To_Unit = ConvertedVar.get()
    
    if From_Unit == "Meters":
        result = ConvertFromMeters(Amount_,To_Unit)
        if result == None:
            _ConvertedAmount.config(text="Invalid Conversion")
        else:
            _ConvertedAmount.config(text=f"Converted Amount:\n{result:.2f} {To_Unit}")
    else:
        _ConvertedAmount.config(text="Invalid Unit for Conversion")
        return
    
window = Tk()
window.title("Converter Application")

#Center The Window
Center_Window(window, width=270, height=230)

#Dropdown variables
ConvertedVar = StringVar()
ToConvertVar = StringVar()

#Amount input
_Amount = Entry(master=window, font=("Arial", 12, "bold"), width=12)
_Amount.grid(row=1, column=0, padx=5, pady=5)

#Dropdowns
_DropdownToConvert = ttk.Combobox(master=window,
                                  values=["Meters", "Kilometers", "Centimeters", "Inches", "Feet", "Grams", "Kilograms", "Ounce", "Pounds"],
                                  textvariable=ToConvertVar,
                                  width=10)
_DropdownToConvert.grid(row=1, column=1, pady=5)

_DropdownConvert = ttk.Combobox(master=window,
                                values=["Meters", "Kilometers", "Centimeters", "Inches", "Feet", "Grams", "Kilograms", "Ounce", "Pounds"],
                                textvariable=ConvertedVar,
                                width=10)
_DropdownConvert.grid(row=2, column=0, padx=5, pady=5)

#Output label
_ConvertedAmount = Label(master=window, text="Converted Amount: ", font=("Arial", 12, "bold"))
_ConvertedAmount.grid(row=4, column=0, padx=5, pady=5)

#Convert button
_ConvertButton = Button(master=window, text="Convert", font=("Arial", 12, "bold"), command=Converted)
_ConvertButton.grid(row=3, column=0, padx=5, pady=5)

window.mainloop()