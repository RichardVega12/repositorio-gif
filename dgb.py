from tkinter import *
ventana=Tk()
ventana.title("DGB")
ventana.geometry("1070x100")
#Creamos la imagen
imagen=PhotoImage(file='D:\PYTHON\DGB\dgb.png')
fondo=Label(ventana,image=imagen).place(x=0,y=0)
ventana.mainloop()