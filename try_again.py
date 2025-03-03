# Feb 27 2025 
# Tkinter practice again 1st window

from tkinter import *
from window import anotherwindow

def secondwin():
    # Window,title and size of it.
    window = Tk()
    window.title("Warning!")
    window.geometry("350x180")

    # icon na warnig sa taas (di ko pa gets masyado yung sa false na part)
    icon = PhotoImage(file= "D:\ITCS103_GARCIA_1A\TryCodes\warning.png")    
    window.iconphoto(False, icon) 

    # Text na nakalagay sa window
    Label(window, text="This might a while.").place(relx=0.1, rely=0.2)
    Label(window, text="Are you sure do you want to continue?").place(relx=0.1, rely=0.35)

    # Pag clinick ang mga button
    def ifYes():
        if Button(yes):
            window.destroy()
            anotherwindow()
        else:
            pass
    def ifNo():        
            if Button(no):
                window.destroy()

    #Button (Inaaral ko palang din yung .place at relx and y and lastly yung anchor)  
    yes = Button(window, text="Yes", width=5, command=ifYes).place(relx=0.6, rely=0.7, anchor="se")
    no = Button(window, text="No", width=5, command=ifNo).place(relx=0.75, rely=0.7, anchor="se")

    # Yung pang call ng window para lumabas
    window.mainloop()