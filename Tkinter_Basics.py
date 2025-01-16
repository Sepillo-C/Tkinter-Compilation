from tkinter import *

window = Tk() #Makes the window

window.title("First GUI") #Title for the application

icon = PhotoImage(file='logo.png') #For setting the path to the logo
window.iconphoto(True,icon) #For setting the logo for the application
window.config(background="#fffff2") #Background color of the application


window.mainloop() #Runs the window