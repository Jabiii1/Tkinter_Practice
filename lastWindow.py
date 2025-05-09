from tkinter import *

def infoClicked():
    lastwindow = Tk()
    lastwindow.title("Checking Information")
    
    def center_window(lastwindow, width, height):
        # Get the screen width and height
        screen_width = lastwindow.winfo_screenwidth()
        screen_height = lastwindow.winfo_screenheight()

        # Calculate the position for the window to be centered
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        
        # Set the geometry of the window with the calculated position
        lastwindow.geometry(f'{width}x{height}+{position_left}+{position_top}')

    window_width = 350
    window_height = 500

    center_window(lastwindow, window_width, window_height)
    lastwindow.resizable(FALSE,FALSE)
    
    Name = Label(lastwindow,text="hI")
    Name.pack()
    
    lastwindow.lift()
    lastwindow.mainloop()