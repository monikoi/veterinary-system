from tkinter import *
import tkinter as tk
from tkinter import messagebox
from registro import Citas
from cancelaciones import Cancelar
from mascota import Registros_M
from estadisticass import Estadistica_mensual
import sys
import os
from PIL import Image, ImageTk

class Menu(tk.Frame): #clase manu
    def __init__(self, padre, controlador):  #constructor de la clase
        super().__init__(padre)
        self.controlador = controlador #llama a los mtodos del controlador 
        self.pack()
        self.place(x=0, y=0, width=1100, height=650) #tamaño de la pantalla
        self.configure(background="#94e1b7") 
        tk.Label(self, text="Bienvenido ", background= "#94e1b7",fg="#0C3B21",font=("Courier", 80)).place(x=250, y=100)
        #RUTA DE IMAGEN 
        ruta_base = os.path.dirname(os.path.abspath(__file__))  # Carpeta donde está el archivo actual
        ruta_imagen = os.path.join(ruta_base, "Banner.png")

        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((200, 650))  #ajusta el tamaño 
        self.imagen_tk = ImageTk.PhotoImage(imagen)  # usa self. para evitar que se borre

        label_imagen = tk.Label(self, image=self.imagen_tk, bg="#94e1b7")
        label_imagen.place(x=0, y=0)  # Ajusta posición
        self.widgets()
        
#función que limpia los frames cada que sea desea abrir nuevamente 
    def show_frames(self, opc):
        for widget in self.winfo_children(): # se hace referencia al frame actual, y 
            #la función winfo_children retorna todos lo frames, label... que existan en este frame
            if isinstance(widget, opc):#condición que verifica que sean widgets de tipo de la clase 
                widget.destroy()


        frame=opc(self) 
        frame.config(bg="#f5f5dc", highlightthickness=1)#h - grosor
        frame.place(x=200, y=40, width=900, height=610) #tamaño y posición del frame
        frame.tkraise() #lo posiciona al frente
        
#funciones que mandan que abren el frame de cada boton
    def citas(self):
        self.show_frames(Citas)

    def cancelaciones(self):
        self.show_frames(Cancelar)   
    
    def mascota(self):
        self.show_frames(Registros_M)
    
    def estadisticas(self):
        self.show_frames(Estadistica_mensual)
    
    def cerrar(self): #función del boton de salir en el menu
        resp = messagebox.askquestion("Salir", "¿Desea salir?") #mesaje de confirmación de salir
        from inicio import Login
        if resp == 'yes':
            self.controlador.show_frame(Login)
            #self.destroy()

    def widgets(self): #función de widgets , botones de la barra de menu
        frame_aux= tk.Frame(self)
        frame_aux.place(x=0, y=0, width=1100, height=40) #frame para los botones
        #botones que son parte del menu y cada uno tiene  una llamada a su función 
        self.btn_Citas= Button (frame_aux, fg="white", text="Citas", font=("Times New Roman",12), command=self.citas, bg="#3cb371")
        self.btn_Citas.place(x=200, y=0, width=200)
        self.btn_Cancelar= Button (frame_aux, fg="white", text="Cancelaciones", font=("Times New Roman",12),bg="#3cb371",command=self.cancelaciones)
        self.btn_Cancelar.place(x=400, y=0, width=200)
        self.btn_mascota= Button (frame_aux, fg="white", text="Registros", font=("Times New Roman",12),bg="#3cb371",command=self.mascota)
        self.btn_mascota.place(x=600, y=0, width=200)
        self.btn_estadisticas= Button (frame_aux, fg="white", text="Estadisticas", font=("Times New Roman",12),bg="#3cb371",command=self.estadisticas)
        self.btn_estadisticas.place(x=800, y=0, width=200)
        self.btn_cerrar = Button (frame_aux, fg="white", text="Salir", font=("Times New Roman",12),bg="#3cb371",command=self.cerrar)
        self.btn_cerrar.place(x=1000, y=0, width=100)