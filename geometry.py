from tkinter import *
def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position for the window to be centered
    position_top = int(screen_height / 2 - height / 2)
    position_left = int(screen_width / 2 - width / 2)

    # Set the geometry of the window with the calculated position
    window.geometry(f'{width}x{height}+{position_left}+{position_top}')

# Create the main window
mainWindow = Tk()

# Set the size of the window
window_width = 325
window_height = 500

# Center the window

