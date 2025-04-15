# Feb 27 2025 
# Tkinter practice again 1st window

from tkinter import *
from tkinter import ttk
from lastWindow import infoClicked

def loadingWindow():
    loadWindow = Tk()
    loadWindow.title("Loading")
    loadWindow.configure(bg="lightblue")
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

    center_window(loadWindow, window_width, window_height)
    
    def clicked():
        loadWindow.destroy()
        infoClicked()
        
    
    def change_1():
        infos.config(text="Analyzing Complete!", font="Arial, 15", bg="lightblue")
        infos.place_configure(x=80, y=60)
        chkInfo = Button(loadWindow, text="Check Info", command=clicked).place_configure(x=140, y=100)
        
        
    
    def change_2():
        infos.config(text="Checking Civil Status...")
        
        loadWindow.after(1878, change_1)
    
    def change_3():
        infos.config(text="Scanning your Address...")
        
        loadWindow.after(1000, change_2)
    
    def change_4():
        infos.config(text="Checking Typos...")
        
        loadWindow.after(1000, change_3)
    
    def change_5():
        infos.config(text="Scanning Errors...")
        
        loadWindow.after(1000, change_4)
    # Texts
    wait = Label(loadWindow, text="\n\nPlease wait a while.", bg="lightblue")
    wait.pack(padx=0, pady=1)
    wait.after(5878, wait.destroy)
    
    infos = Label(loadWindow, text="Analyzing your Personal Details...", bg="lightblue")
    infos.pack(padx=0, pady=2)
    

    
    # Progress Bar
    # Pagdeterminate start to finnish = mas ayos pag sa mga formal
    # Pag indeterminate loading na di mo makikita ang progress = informal 

    def stopLoad():
        loading.stop()   #Para mag stop yun loading
        loading.pack_forget() #Para mawala yung loading 


    loading = ttk.Progressbar(loadWindow, orient=HORIZONTAL, length=200, mode="determinate")
    loading.pack(pady=3)
    loading.start()
    loadWindow.after(1000, change_5)
    
    loadWindow.after(5878,stopLoad) #Di ko pa masyadong gets yung num at function na after

    # Para auto nasa top yung window
    loadWindow.lift()
    loadWindow.mainloop()
