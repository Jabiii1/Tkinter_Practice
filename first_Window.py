# tkinter personal info window
# March 4 2025
# di pa nagana pag praktikal pero a practice is practice

# imports
from tkinter import *
from tkinter import ttk
from try_again import warnWin
    
# window/title/size/Main Label
mainWindow = Tk()
mainWindow.title("Personal Information")
mainWindow.configure(bg="lightblue")
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
window_height = 500

center_window(mainWindow, window_width, window_height)
mainWindow.resizable(FALSE,FALSE)

Label(mainWindow, text="PERSONAL INFORMATION\n", font="Arial",justify="center", bg="lightblue").place(x=80, y=10, )

# Icon (medyo inaaral ko pa)
icon = PhotoImage(file= "C:\\Users\\jayve\\Documents\\GitHub\\Tkinter_Practice\\info.png")    
mainWindow.iconphoto(False, icon) 

# function pag clinick yung done button
def Inclick():
    if Button(Submit):
        mainWindow.destroy()
        warnWin()
    else:
        pass
    


# Personal Info
Label(mainWindow, text='First Name:', bg="lightblue").place(x=8, y=43)
Fname = Entry(mainWindow, width=20 ,justify="center").place(x=80, y=43)

Label(mainWindow, text='Middle Name:', bg="lightblue").place(x=1, y=63)
Lname = Entry(mainWindow, width=20  ,justify="center").place(x=80, y=63)

Label(mainWindow, text='Last Name:', bg="lightblue").place(x=8, y=83)
Lname = Entry(mainWindow, width=20  ,justify="center").place(x=80, y=83)


Label(mainWindow, text="Age:", bg="lightblue").place(x=220, y=43)
age = Entry(mainWindow, width=10, justify="center").place(x=270, y=43)


# Combobox (di pako sanay pero very nays to)
Label(mainWindow, text="Gender:", bg="lightblue").place(x=220, y=63)
age = ttk.Combobox(mainWindow, values=["Male", "Female","Other"] , width=7, state="readonly" ,justify="center").place(x=270, y=63)

Label(mainWindow, text="Course:", bg="lightblue").place(x=220, y=83)
age = ttk.Combobox(mainWindow, values=["BSIT", "ABELS","BSSW", "BSA", "BTVTEd" ,"BSE","DHRS", "BSAIS", "BSPA"] , width=7, state="readonly" ,justify="center").place(x=270, y=83)

Label(mainWindow, text="ADDRESS",font="Arial", bg="lightblue").place(x=130, y=113)

# # Social Accounts
# Label(mainWindow, text="Social Accounts", font="Arial").grid(row=20, column=1)
# Label(mainWindow, text="Email:").grid(row=21)
# email = Entry(mainWindow).grid(row=22,column=1)
# Label(mainWindow, text="Facebook:").grid(row=23)
# facebook = Entry(mainWindow).grid(row=24,column=1)


# Nakakatamad na part (pinag effortan/Challenge)

regions = ["Luzon","Visayas","Mindanao"]

# List and Dictionary (nakakayawa to)
provinces = {
        "Luzon": [
            "Ilocos Norte", "Ilocos Sur", "La Union", "Pangasinan",
            "Batanes", "Cagayan", "Isabela", "Nueva Vizcaya", "Quirino",
            "Aurora", "Bataan", "Bulacan", "Nueva Ecija", "Pampanga", "Tarlac", "Zambales",
            "Batangas", "Cavite", "Laguna", "Quezon", "Rizal",
            "Marinduque", "Occidental Mindoro", "Oriental Mindoro", "Palawan", "Romblon",
            "Abra", "Apayao", "Benguet", "Ifugao", "Kalinga", "Mountain Province",
            "Albay", "Camarines Norte", "Camarines Sur", "Catanduanes", "Masbate", "Sorsogon"
        ],
        "Visayas": [
            "Aklan", "Antique", "Capiz", "Guimaras", "Iloilo",
            "Bohol", "Cebu", "Negros Oriental", "Siquijor",
            "Biliran", "Eastern Samar", "Leyte", "Northern Samar", "Samar", "Southern Leyte"
        ],  
        "Mindanao": [
            "Zamboanga del Norte", "Zamboanga del Sur", "Zamboanga Sibugay",
            "Bukidnon", "Camiguin", "Lanao del Norte", "Misamis Occidental", "Misamis Oriental",
            "Davao de Oro", "Davao del Norte", "Davao del Sur", "Davao Occidental", "Davao Oriental",
            "Cotabato", "Sarangani", "South Cotabato", "Sultan Kudarat",
            "Agusan del Norte", "Agusan del Sur", "Dinagat Islands", "Surigao del Norte", "Surigao del Sur",
            "Basilan", "Lanao del Sur", "Maguindanao del Norte", "Maguindanao del Sur", "Sulu", "Tawi-Tawi"
        ]
    }

Label(mainWindow, text="Region:",bg="lightblue").place(x=8, y=143)
RegionCbox = ttk.Combobox(mainWindow, width=10 ,values=regions,justify="center", state="readonly")
RegionCbox.place(x=55, y=143)          #para mabind kelangan ihiwalay etong .place .grid ewan lang sa .pack


Label(mainWindow, text="Province:",bg="lightblue").place(x=153, y=143)
ProvinceCbox = ttk.Combobox(mainWindow, width=15 ,justify="center", state="readonly")
ProvinceCbox.place(x=210, y=143)        #para mabind kelangan ihiwalay etong .place .grid ewan lang sa .pack


def update(event):
    selectedRegion = RegionCbox.get()    #Nag declare ako ng variable para mas madali maintindihan
    if selectedRegion in provinces:
        ProvinceCbox["values"] = provinces[selectedRegion]
        
    
RegionCbox.bind("<<ComboboxSelected>>", update)


# Label(mainWindow, text='Postal Code:', bg="lightblue").place(x=8, y=143)
# Fname = Entry(mainWindow, width=10 ,justify="center").place(x=80, y=143)

# May 3 types ang state: normal = editable, readonly = read only, disabled = di nacliclick(pede sa conditional)

# Done Button
Submit = Button(mainWindow, text="Submit", command=Inclick).place(x=153, y=183)
mainWindow.mainloop()
    

