# tkinter personal info window
# March 4 2025
# di pa nagana pag praktikal pero a practice is practice

# imports
from tkinter import *
from tkinter import ttk
from try_again import warning_sign


# window/title/size/Main Label
mainWindow = Tk()
mainWindow.title("Personal Information")
mainWindow.configure(bg="lightblue")
def center_window(mainwindow, width, height):
    # Get the screen width and height
    screen_width = mainwindow.winfo_screenwidth()
    screen_height = mainwindow.winfo_screenheight()

    # Calculate the position for the window to be centered
    position_top = int(screen_height / 2 - height / 2)
    position_left = int(screen_width / 2 - width / 2)
    
    # Set the geometry of the window with the calculated position
    mainwindow.geometry(f'{width}x{height}+{position_left}+{position_top}')

window_width = 350
window_height = 500

center_window(mainWindow, window_width, window_height)
mainWindow.resizable(FALSE,FALSE)

Label(mainWindow, text="PERSONAL INFORMATION\n", font="Arial",justify="center", bg="lightblue").place(x=80, y=10, )

# Icon (medyo inaaral ko pa)
icon = PhotoImage(file= "D:\\ITCS103_GARCIA_1A\\Tkinter_Practice\\info.png")    
mainWindow.iconphoto(False, icon) 

# function pag clinick yung done button
def Inclick():
    if Button(Submit):
        mainWindow.destroy()
        warning_sign()
    else:
        pass
    


# Personal Info
Label(mainWindow, text='First Name:', bg="lightblue").place(x=8, y=43)
Fname = Entry(mainWindow, width=20 ,justify="center")
Fname.place(x=80, y=43)

Label(mainWindow, text='Middle Name:', bg="lightblue").place(x=1, y=63)
Mname = Entry(mainWindow, width=20  ,justify="center").place(x=80, y=63)

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


# Nakakatamad na part (pinag effortan/Challenge para sa improvements)

island = ["Luzon","Visayas","Mindanao"]

region = {
    "Luzon": ["Region-I", "Region-II", "Region-III", "Region-IV-A", "Region-V", "NCR", "CAR", "MIMAROPA"],
    
    "Visayas": ["Western Visayas-VI", "Central Visayas-VII", "Eastern Visayas-VIII"],
    
    "Mindanao": ["Region-IX", "Region-X", "Region-XI", "Region-XII", "BARMM", "Region-XIII"]
    
}

provinces = {
        # Luzon
        "Region-I": ["Ilocos Norte", "Ilocos Sur", "La Union", "Pangasinan"],
        
        "Region-II":["Batanes", "Cagayan", "Isabela", "Nueva Vizcaya", "Quirino"],
        
        "Region-III":["Aurora", "Bataan", "Bulacan", "Nueva Ecija", "Pampanga", "Tarlac", "Zambales"],
        
        "Region-IV-A":["Batangas", "Cavite", "Laguna", "Quezon", "Rizal"],
            
        "Region-V":["Albay", "Camarines Norte", "Camarines Sur", "Catanduanes", "Masbate", "Sorsogon"],
        
        "NCR":["Metro Manila"],
        
        "CAR":["Abra", "Apayao", "Benguet", "Ifugao", "Kalinga", "Mountain Province"],
        
        "MIMAROPA":["Marinduque", "Occidental Mindoro", "Oriental Mindoro", "Palawan", "Romblon"],
        
        # Visayas
        "Western Visayas-VI":["Aklan", "Antique", "Capiz", "Guimaras", "Iloilo","Negros Oriental"],
        
        "Central Visayas-VII":["Bohol", "Cebu", "Negros Oriental", "Siquijor"],
            
        "Eastern Visayas-VIII":["Biliran", "Eastern Samar", "Leyte", "Northern Samar", "Samar", "Southern Leyte"],
        
        # "Mindanao"
        "Region-IX": ["Zamboanga del Norte", "Zamboanga del Sur", "Zamboanga Sibugay"],
        
        "Region-X":["Bukidnon", "Camiguin", "Lanao del Norte", "Misamis Occidental", "Misamis Oriental"],
        
        "Region-XI":["Davao de Oro", "Davao del Norte", "Davao del Sur", "Davao Occidental", "Davao Oriental"],
        
        "Region-XII":["Cotabato", "Sarangani", "South Cotabato", "Sultan Kudarat"],

        "BARMM":["Basilan", "Lanao del Sur", "Maguindanao del Norte", "Maguindanao del Sur", "Sulu", "Tawi-Tawi"],
        
        "Region-XIII":[ "Agusan del Norte", "Agusan del Sur", "Dinagat Islands", "Surigao del Norte", "Surigao del Sur",]
    }

cities = {
        "Ilocos Norte": ["Laoag", "Batac"],
        
        "Ilocos Sur": ["Vigan", "Candon", "Tagudin"],
        
        "La Union": ["San Fernando", "Bauang", "Agoo", "Naguilian"],
        
        "Pangasinan": ["Dagupan", "San Carlos", "Urdaneta", "Alaminos", "Lingayen", "Calasiao"],
        
        "Batanes": ["Basco", "Itbayat"],
        
        "Cagayan": ["Tuguegarao", "Aparri", "Ballesteros", "Claveria"],
        
        "Isabela": ["Cauayan", "Ilagan", "Santiago", "Roxas", "San Mateo"],
        
        "Nueva Vizcaya": ["Bayombong", "Solano", "Bagabag"],
        
        "Quirino": ["Cabarroguis", "Diffun", "Maddela"],
        
        "Aurora": ["Baler", "Maria Aurora", "Dipaculao"],
        
        "Bataan": ["Balanga", "Dinalupihan", "Orion", "Mariveles"],
        
        "Bulacan": ["Malolos", "Meycauayan", "San Jose del Monte", "Bocaue", "Marilao", "Santa Maria"],
        
        "Nueva Ecija": ["Cabanatuan", "Gapan", "Palayan", "San Jose", "Talavera", "Science City of Muñoz"],
        
        "Pampanga": ["Angeles", "San Fernando", "Mabalacat", "Apalit"],
        
        "Tarlac": ["Tarlac City", "Concepcion", "Capas"],
        
        "Zambales": ["Olongapo", "Iba", "Subic", "Botolan"],
        
        "Batangas": ["Batangas City", "Lipa", "Tanauan", "San Juan", "Nasugbu"],
        
        "Cavite": ["Tagaytay", "Trece Martires", "Dasmariñas", "Imus", "Bacoor", "General Trias"],
        
        "Laguna": ["San Pablo", "Calamba", "Santa Rosa", "Biñan", "Cabuyao", "Los Baños"],
        
        "Quezon": ["Lucena", "Tayabas", "Sariaya", "Candelaria"],
        
        "Rizal": ["Antipolo", "Cainta", "Binangonan", "Taytay"],
        
        "Marinduque": ["Boac", "Santa Cruz", "Mogpog"],
        
        "Occidental Mindoro": ["Mamburao", "San Jose", "Sablayan"],
        
        "Oriental Mindoro": ["Calapan", "Pinamalayan", "Naujan"],
        
        "Palawan": ["Puerto Princesa", "Coron", "El Nido", "Roxas"],
        
        "Romblon": ["Romblon", "Odiongan", "San Fernando"],
        
        "Abra": ["Bangued", "Tineg"],
        
        "Apayao": ["Kabugao", "Conner", "Luna"],
        
        "Benguet": ["Baguio", "La Trinidad", "Itogon"],
        
        "Ifugao": ["Lagawe", "Kiangan", "Banaue"],
        
        "Kalinga": ["Tabuk", "Tinglayan"],
        
        "Mountain Province": ["Bontoc", "Sagada", "Bauko"],
        
        "Albay": ["Legazpi", "Tabaco", "Ligao", "Daraga"],
        
        "Camarines Norte": ["Daet", "Jose Panganiban", "Basud"],
        
        "Camarines Sur": ["Naga", "Iriga", "Pili", "Caramoan"],
        
        "Catanduanes": ["Virac", "San Andres"],
        
        "Masbate": ["Masbate City", "Aroroy", "Ticao"],
        
        "Sorsogon": ["Sorsogon City", "Bulusan", "Gubat"],
        
        "Aklan": ["Kalibo", "Malay", "Numancia"],
        
        "Antique": ["San Jose de Buenavista", "Sibalom", "Culasi"],
        
        "Capiz": ["Roxas City", "Pilar", "Panay"],
        
        "Guimaras": ["Jordan", "Buenavista", "Nueva Valencia"],
        
        "Iloilo": ["Iloilo City", "Passi", "Pototan", "Jaro"],
        
        "Bohol": ["Tagbilaran", "Ubay", "Talibon"],
        
        "Cebu": ["Cebu City", "Lapu-Lapu", "Mandaue", "Carcar", "Danao"],
        
        "Negros Oriental": ["Dumaguete", "Bais", "Tanjay", "Bayawan"],
        
        "Siquijor": ["Siquijor", "Larena", "Lazi"],
        
        "Biliran": ["Naval", "Kawayan", "Biliran"],
        
        "Eastern Samar": ["Borongan", "Guiuan", "Oras"],
        
        "Leyte": ["Tacloban", "Ormoc", "Baybay", "Palo"],
        
        "Northern Samar": ["Catarman", "Allen", "Bobon"],
        
        "Samar": ["Catbalogan", "Calbayog", "Gandara"],
        
        "Southern Leyte": ["Maasin", "Sogod", "Hinunangan"],
    
        "Zamboanga del Norte": ["Dipolog", "Dapitan", "Polanco"],
        
        "Zamboanga del Sur": ["Pagadian", "Molave", "Labangan"],
        
        "Zamboanga Sibugay": ["Ipil", "Kabasalan", "Diplahan"],
        
        "Bukidnon": ["Malaybalay", "Valencia", "Maramag", "Manolo Fortich"],
        
        "Camiguin": ["Mambajao", "Catarman"],
        
        "Lanao del Norte": ["Iligan", "Kauswagan", "Tubod"],
        
        "Misamis Occidental": ["Oroquieta", "Ozamis", "Tangub"],
        
        "Misamis Oriental": ["Cagayan de Oro", "Gingoog", "Tagoloan"],
        
        "Davao de Oro": ["Nabunturan", "Monkayo", "Compostela"],
        
        "Davao del Norte": ["Tagum", "Panabo", "Samal"],
        
        "Davao del Sur": ["Davao City", "Digos", "Santa Cruz"],
        
        "Davao Occidental": ["Malita", "Jose Abad Santos"],
        
        "Davao Oriental": ["Mati", "Baganga", "Cateel"],
        
        "Cotabato": ["Kidapawan", "M'lang", "Kabacan"],
        
        "Sarangani": ["Alabel", "Glan", "Malapatan"],
        
        "South Cotabato": ["Koronadal", "General Santos", "Tupi"],
        
        "Sultan Kudarat": ["Isulan", "Tacurong", "Lutayan"],
        
        "Agusan del Norte": ["Butuan", "Cabadbaran", "Nasipit"],
        
        "Agusan del Sur": ["Bayugan", "Prosperidad", "San Francisco"],
        
        "Dinagat Islands": ["San Jose", "Loreto"],
        
        "Surigao del Norte": ["Surigao City", "Siargao", "Claver"],
        
        "Surigao del Sur": ["Tandag", "Bislig", "Lianga"],
        
        "Basilan": ["Isabela City", "Lamitan"],
        
        "Lanao del Sur": ["Marawi", "Balindong", "Malabang"],
        
        "Maguindanao del Norte": ["Datu Odin Sinsuat", "Barira"],
        
        "Maguindanao del Sur": ["Buluan", "Pagalungan"],
        
        "Sulu": ["Jolo", "Patikul", "Parang"],
        
        "Tawi-Tawi": ["Bongao", "Sitangkai", "Panglima Sugala"]
    }

Label(mainWindow, text="Island:",bg="lightblue").place(x=8, y=143)
IslandCbox = ttk.Combobox(mainWindow, width=15 ,values=island,justify="center", state="readonly")
IslandCbox.place(x=63, y=143)          #para mabind kelangan ihiwalay etong .place .grid ewan lang sa .pack
IslandCbox.set("Select Island")        #set is parang preview or guide para sa user

Label(mainWindow, text="Region:",bg="lightblue").place(x=180, y=143)
RegionCbox = ttk.Combobox(mainWindow, width=15 ,justify="center", state="readonly")
RegionCbox.place(x=225, y=143)  
RegionCbox.set("Select Region") 

Label(mainWindow, text="Province:",bg="lightblue").place(x=8, y=170)
ProvinceCbox = ttk.Combobox(mainWindow, width=15 ,justify="center", state="readonly")
ProvinceCbox.place(x=63, y=170)        
ProvinceCbox.set("Select Province")

Label(mainWindow, text="City:",bg="lightblue").place(x=180, y=170)
CityCbox = ttk.Combobox(mainWindow, width=15 ,justify="center", state="readonly")
CityCbox.place(x=225, y=170) 
CityCbox.set("Select City")

# Bind na tinuro ni sir

def Island_Update(event):
    selectedIsland = IslandCbox.get()
    if selectedIsland in region:
        RegionCbox["values"] = region[selectedIsland]
        

def Region_Update(event):
    selectedRegion = RegionCbox.get()  
    if selectedRegion in provinces:
        ProvinceCbox["values"] = provinces[selectedRegion] 
        
def Province_Update(event):
    selectedProvince = ProvinceCbox.get()  
    if selectedProvince in cities:
        CityCbox["values"] = cities[selectedProvince]  

IslandCbox.bind("<<ComboboxSelected>>", Island_Update)
RegionCbox.bind("<<ComboboxSelected>>", Region_Update)
ProvinceCbox.bind("<<ComboboxSelected>>", Province_Update)
    



# Label(mainWindow, text='Postal Code:', bg="lightblue").place(x=8, y=143)
# Fname = Entry(mainWindow, width=10 ,justify="center").place(x=80, y=143)

# May 3 types ang state: normal = editable, readonly = read only, disabled = di nacliclick(pede sa conditional)

# Done Button
Submit = Button(mainWindow, text="Submit", command=Inclick).place(x=153, y=250)
mainWindow.mainloop()
    
