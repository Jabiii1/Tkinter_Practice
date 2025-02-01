from tkinter import * #para lahat na sa tkinter ay iimport 
window = Tk()         #eto naman ay yung window na lalabas pag kinall
window.title("First try tk!")  #title sa taas ng window
window.geometry("400x300")     #para fix agad yung size nya pag nirun mo  (adjustable)


#label ay sa text na ilalagay mo sa window self explanatory na yung iba
m = Label(window, text ="Jabii" ,height=15,font="Arial") 
m.pack()  #para pagisahin sila




window.mainloop() #pang call ng window