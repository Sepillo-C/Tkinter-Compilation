from tkinter import *

_Perfume = ["YSL","Chanel", "Dior"]
#Index Value: 0             1           2

def preference():
    if(x.get()==0):
        print('I prefer YSL Y')
    elif(x.get()==1):
        print('I prefer Bleu De Chanel')
    elif(x.get()==2):
        print('I prefer Dior Sauvage')
    else:
        print('How!?')




window = Tk()

ysl_logo = PhotoImage(file='C:\\Users\\Administrator\Desktop\\Tkinter-Compilation\\Tk Radiobutton\\Logo\\ysl.png')
_ysl_logo = ysl_logo.subsample(5,5)
chanel_logo = PhotoImage(file='C:\\Users\\Administrator\Desktop\\Tkinter-Compilation\\Tk Radiobutton\\Logo\\chanel.png')
_chanel_logo = chanel_logo.subsample(8,8)
dior_logo = PhotoImage(file='C:\\Users\\Administrator\Desktop\\Tkinter-Compilation\\Tk Radiobutton\\Logo\\dior.png')
_dior_logo = dior_logo.subsample(11,11)

_Perfumelogo = [_ysl_logo, _chanel_logo, _dior_logo]    #List the images for the logo

x = IntVar()


for index in range(len(_Perfume)):
    radioB = Radiobutton(window,
                        text=_Perfume[index],  #Adds text the radiobuttons
                        variable=x, #Groups the radio buttons together (if they share the same variable)
                        value=index, #Assigns each radiobutton a different value
                        padx= 20,   #Adds padding in the x-axis ("pady=" for y-axis)
                        font=('Times New Roman', 30, 'bold'),
                        fg='light blue',
                        bg='#FDFD96',
                        activebackground='light blue',
                        activeforeground='#FDFD96',
                        image = _Perfumelogo[index], #Adds image to radiobutton
                        compound=RIGHT,
                        indicatoron=0, #Eliminates the circles indicators
                        width= 280,  #This also affects the indicatoron
                        command= preference #Calls the function
                        )
    
    radioB.pack(anchor=W)   #Anchors lines up the widgets

window.mainloop()