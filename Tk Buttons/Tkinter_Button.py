from tkinter import *

count = 0

def click():
    global count
    count += 1
    label.config(text=count)    #Displays the output of the function in the label

window = Tk()

clicking = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter\\Tk Buttons\\click.png')
clickresized = clicking.subsample(3, 3) #Resizing the image

button1 = Button(window,
                 text='Click Me',
                 )

button1.config(command=click, #Performs the called function
               font=('Ariel',30,'italic'), #Custimize the font, size, and type of the text
               fg='White', #Static Foreground
               bg='#088F8F', #Static Background
               activebackground='#C70039', 
               activeforeground='Black',
               image=clickresized, #Displays the image in the button
               compound='right', #Place the button in the called position
               )

label = Label(window,
              text=count
              )
label.config(font=('Ariel',30,'bold'),
            fg='black',
            bg='#C70039',
            )
label.pack()

button1.pack()  #Displaying the button

window.mainloop()