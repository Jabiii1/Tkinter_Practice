# tkinter personal info window
# March 4 2025
# di pa nagana pag praktikal pero a practice is practice

# imports
from tkinter import *
from try_again import secondwin

# window/title/size/Main Label
window = Tk()
window.title("Personal Information")
window.geometry("350x500")
info = Label(window, text="PERSONAL INFORMATION\n", font="Arial").grid(row=0, column=1)

# Icon (medyo inaaral ko pa)
icon = PhotoImage(file= "D:\ITCS103_GARCIA_1A\TryCodes\info.png")    
window.iconphoto(False, icon) 

# function pag clinick yung done button
def Inclick():
    if Button(done):
        window.destroy()
        secondwin()
    else:
        pass

# First Name and Last Name and Age
Label(window, text='First Name:').grid(row=1)
Fname = Entry(window).grid(row=1, column=1)

Label(window, text='Last Name:').grid(row=2)
Lname = Entry(window).grid(row=2, column=1)

Label(window, text="Age:").grid(row=3)
age = Entry(window).grid(row=3, column=1)



# Gender (medyo di ko pa to gets pero mostly ng function nya ay nagegets ko naman)
int = IntVar()
Label(window, text="\nGender:", font="Arial").grid(row=5, column=1)
Gone = Radiobutton(window, text='Male', variable=int, value=1).grid(row=6)
Gtwo = Radiobutton(window, text='Female', variable=int, value=2).grid(row=7)
Gthree = Radiobutton(window, text='Other', variable=int, value=3).grid(row=8)

# Social Accounts
Label(window, text="\nSocial Accounts", font="Arial").grid(row=9, column=1)
Label(window, text="Email:").grid(row=10)
email = Entry(window).grid(row=10,column=1)
Label(window, text="Facebook:").grid(row=11)
facebook = Entry(window).grid(row=11,column=1)


# Done Button
done = Button(window, text="done", command=Inclick).grid(row=12,column=1)


window.mainloop()