from tkinter import *

def submit():
    username = entry.get()  #Gets the information that is entered
    print(f'Hello, {username}') #Prints the said information

window = Tk()

submition = Button(window,text='Submit!',
                   command= submit
                   )

entry = Entry() #Makes the entry widget
entry.config(font=('Arial', #Font Style
                    30, #Font Size
                    'bold'),   #Font Format
                    bg='black', #Background of entry
                    fg='white', #Foreground of entry
                    # show='*',   #Replaces the letters with the selected character
                    )
# entry.insert(0,'Enter Something') #Default text in the entry

entry.pack()    
submition.pack()

window.mainloop()