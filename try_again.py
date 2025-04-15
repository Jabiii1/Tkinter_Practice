# Feb 27 2025 
# Tkinter practice again 1st window

from tkinter import *
from window import loadingWindow


def warning_sign():
    # Window,title and size of it.
    tryWindow = Tk()
    tryWindow.title("Warning!")
    tryWindow.configure(bg="lightblue")

    def center_window(tryWindow, width, height):
        # Get the screen width and height
        screen_width = tryWindow.winfo_screenwidth()
        screen_height = tryWindow.winfo_screenheight()

        # Calculate the position for the window to be centered
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        
        # Set the geometry of the window with the calculated position
        tryWindow.geometry(f'{width}x{height}+{position_left}+{position_top}')

    window_width = 350
    window_height = 180

    center_window(tryWindow, window_width, window_height)

    tryWindow.lift()
    # icon na warnig sa taas (di ko pa gets masyado yung sa false na part)
    icon = PhotoImage(file= "D:\\ITCS103_GARCIA_1A\\Tkinter_Practice\\warning.png")    
    tryWindow.iconphoto(False, icon) 

    # Text na nakalagay sa window
    Label(tryWindow, text="This might a while.",bg="lightblue").place(relx=0.1, rely=0.2)
    Label(tryWindow, text="Are you sure do you want to continue?",bg="lightblue").place(relx=0.1, rely=0.35)

    # Pag clinick ang mga button
    def ifYes():
        if Button(yes):
            tryWindow.destroy()
            loadingWindow()
        else:
            pass
    def ifNo():        
        if Button(no):
            tryWindow.destroy()
        else:
            pass
                

    #Button (Inaaral ko palang din yung .place at relx and y and lastly yung anchor)  
    yes = Button(tryWindow, text="Yes", width=5, command=ifYes).place(relx=0.6, rely=0.7, anchor="se")
    no = Button(tryWindow, text="No", width=5, command=ifNo).place(relx=0.75, rely=0.7, anchor="se")

    # Yung pang call ng window para lumabas
    tryWindow.mainloop()