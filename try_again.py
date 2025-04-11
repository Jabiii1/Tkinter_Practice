# Feb 27 2025 
# Tkinter practice again 1st window

from tkinter import *
from window import loadingWindow


def secondwin():
    # Window,title and size of it.
    window = Tk()
    window.title("Warning!")

    def center_window(window, width, height):
        # Get the screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate the position for the window to be centered
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        
        # Set the geometry of the window with the calculated position
        window.geometry(f'{width}x{height}+{position_left}+{position_top}')

    window_width = 350
    window_height = 180

    center_window(window, window_width, window_height)

    window.lift()
    # icon na warnig sa taas (di ko pa gets masyado yung sa false na part)
    icon = PhotoImage(file= "C:\\Users\\jayve\\Documents\\GitHub\\Tkinter_Practice\\warning.png")    
    window.iconphoto(False, icon) 

    # Text na nakalagay sa window
    Label(window, text="This might a while.").place(relx=0.1, rely=0.2)
    Label(window, text="Are you sure do you want to continue?").place(relx=0.1, rely=0.35)

    # Pag clinick ang mga button
    def ifYes():
        if Button(yes):
            window.destroy()
            loadingWindow()
        else:
            pass
    def ifNo():        
        if Button(no):
            window.destroy()
        else:
            pass
                

    #Button (Inaaral ko palang din yung .place at relx and y and lastly yung anchor)  
    yes = Button(window, text="Yes", width=5, command=ifYes).place(relx=0.6, rely=0.7, anchor="se")
    no = Button(window, text="No", width=5, command=ifNo).place(relx=0.75, rely=0.7, anchor="se")

    # Yung pang call ng window para lumabas
    window.mainloop()