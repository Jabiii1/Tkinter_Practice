# tkinter personal info window
# March 4 2025
# di pa nagana pag praktikal pero a practice is practice

# imports
from tkinter import *
from try_again import secondwin

# window/title/size/Main Label
mainWindow = Tk()
mainWindow.title("Personal Information")

def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position for the window to be centered
    position_top = int(screen_height / 2 - height / 2)
    position_left = int(screen_width / 2 - width / 2)
    
    # Set the geometry of the window with the calculated position
    window.geometry(f'{width}x{height}+{position_left}+{position_top}')

window_width = 325
window_height = 500

center_window(mainWindow, window_width, window_height)

Label(mainWindow, text="PERSONAL INFORMATION\n", font="Arial").grid(row=0, column=1)

# Icon (medyo inaaral ko pa)
icon = PhotoImage(file= "C:\\Users\\jayve\\Documents\\GitHub\\Tkinter_Practice\\info.png")    
mainWindow.iconphoto(False, icon) 

# function pag clinick yung done button
def Inclick():
    if Button(done):
        mainWindow.destroy()
        secondwin()
    else:
        pass
    
# Done Button
done = Button(mainWindow, text="Submit", command=Inclick).grid(row=12,column=1)

# First Name and Last Name and Age
Label(mainWindow, text='First Name:').grid(row=1)
Fname = Entry(mainWindow).grid(row=1, column=1)

Label(mainWindow, text='Last Name:').grid(row=2)
Lname = Entry(mainWindow).grid(row=2, column=1)

Label(mainWindow, text="Age:").grid(row=3)
age = Entry(mainWindow).grid(row=3, column=1)



# Gender (medyo di ko pa to gets pero mostly ng function nya ay nagegets ko naman)
int = IntVar()
Label(mainWindow, text="\nGender:", font="Arial").grid(row=5, column=1)
Gone = Radiobutton(mainWindow, text="Male", variable=int, value=1).grid(row=6)
Gtwo = Radiobutton(mainWindow, text='Female', variable=int, value=2).grid(row=7)
Gthree = Radiobutton(mainWindow, text='Other', variable=int, value=3).grid(row=8)

# Social Accounts
Label(mainWindow, text="\nSocial Accounts", font="Arial").grid(row=9, column=1)
Label(mainWindow, text="Email:").grid(row=10)
email = Entry(mainWindow).grid(row=10,column=1)
Label(mainWindow, text="Facebook:").grid(row=11)
facebook = Entry(mainWindow).grid(row=11,column=1)

mainWindow.mainloop()
    

