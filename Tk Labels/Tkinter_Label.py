from tkinter import *

window = Tk()
                                                                                    #Name of image
photo = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter\\Tk Labels\\photo\\earth.png') #File location of the image

label = Label(window,
              text="Hello World",   #Text that will appear
              font=("Calibre", 32, 'bold'), #Font Style, Size, Type
              fg='Blue', #Font color
              bg='Yellow', #Background color
              image=photo,   #Puts the image in the label
              compound='bottom' #Image position
              )
label.pack() #Makes the label to come in the GUI
#label.place(x=50,y=50) #Makes the label to come in a designated position

window.mainloop()