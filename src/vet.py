from tkinter import *
from tkinter import ttk
#import tkinter as tk
from menu import Menu
from inicio import Login
#from PIL import Image, ImageTk 
#import sys
#import os


class Principal(Tk):  #clase principal que hereda Tk (Clase Tkinter)
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)#llama a la clase padre
        self.title("Veterinaria ") #titulo de la ventana principal
        self.geometry("1100x650+120+20") #tamaño de la app en pantalla
        self.resizable(False, False) # para que no se pueda redimenzionar
        self.configure(background="#3cb371") #color de la pantalla

        contenedor = Frame(self) #contenedor de un nuevo frame
        contenedor.pack(side=TOP, fill=BOTH, expand=True) # que sus dimensiones ocupen todo el ancho y alto de la pantalla
        

        self.frames={} #almacena los frames de Login y menu
        for i in (Login,Menu):
            frame = i(contenedor, self)
            self.frames[i] = frame 

        self.show_frame(Login)# primer frame en mostrarse al inico de la app
        #self.show_frame(Menu)
        self.style = ttk.Style()
        self.style.theme_use("clam") #estilo de los widgets o frames
    
    def show_frame(self, opc_frame): #función de mostrar frame
        frame= self.frames[opc_frame]
        frame.tkraise() #lleva el frame al frente
        

#para ejecutar la aplicación
def main():
    app = Principal() 
    app.mainloop()
    


if __name__ == "__main__":
   main()


    
