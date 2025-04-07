# Feb 27 2025 
# Tkinter practice again 1st window

from tkinter import *
from tkinter import ttk

def loadingWindow():
    window = Tk()
    window.title("Loading")
    window.geometry("350x180")
        
    # Texts
    wait = Label(window, text="\n\nPlease wait a while.")
    wait.pack(padx=0, pady=1)

    infos = Label(window, text="Analyzing your Personal Details...")
    infos.pack(padx=0, pady=2)

    # Progress Bar
    # Pagdeterminate start to finnish = mas ayos pag sa mga formal
    # Pag indeterminate loading na di mo makikita ang progress = informal 

    def stopLoad():
        loading.stop()   #Para mag stop yun loading
        loading.pack_forget() #Para mawala yung loading 
        Label(window,text="Done!")
        Label.pack

    loading = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode="determinate")
    loading.pack(pady=3)
    loading.start()

    window.after(5578,stopLoad) #Di ko pa masyadong gets yung num at function na after

    # Para auto nasa top yung window
    window.lift()
    window.mainloop()
