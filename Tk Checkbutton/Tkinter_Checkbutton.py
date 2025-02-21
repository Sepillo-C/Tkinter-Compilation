from tkinter import *

def display():
    if (_Int1.get() == 1) and (_Int2.get() == 0):
        print('I like Python')
    elif (_Int1.get() == 0) and (_Int2.get() == 1):
        print('I like Java')
    elif (_Int1.get() == 1) and (_Int2.get() == 1):
        print('I like Both')
    else:
        print("I don't like Python nor Java")
    


window = Tk()

_Int1 = IntVar()  # Variable for Python checkbox
_Int2 = IntVar()  # Variable for Java checkbox

_Pylogo = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter-Compilation\\Tk Checkbutton\\Pythonlogo.png')
_PylogoResized = _Pylogo.subsample(6, 6)
_Javalogo = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\Tkinter-Compilation\\Tk Checkbutton\\Javalogo.png')
_Javalogoresized = _Javalogo.subsample(2, 2)

checkbox1 = Checkbutton(window,
                       text='Python',
                       variable=_Int1,   # Variable for Python
                       onvalue=1,
                       offvalue=0,
                       command=display
                       )
checkbox1.config(font=('Arial',
                      30, 'bold'),
                      fg='blue',
                      bg='yellow',
                      activebackground='blue',
                      activeforeground='yellow',
                      image=_PylogoResized,
                      compound='left'
                      )

checkbox2 = Checkbutton(window,
                       text='Java',
                       variable=_Int2,   # Variable for Java
                       onvalue=1,
                       offvalue=0,
                       command=display
                       )
checkbox2.config(font=('Arial',
                      30, 'bold'),
                      fg='orange',
                      bg='white',
                      activebackground='white',
                      activeforeground='orange',
                      image=_Javalogoresized,
                      compound='left'
                      )


checkbox1.pack()
checkbox2.pack()

window.mainloop()
