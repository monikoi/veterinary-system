from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk 


class Login (tk.Frame):
    def __init__(self, padre, controlador): #constructor padre el que inserta el frame y el controlador referencia a una clase principal o gestor de pantallas, que se usa para cambiar de una pantalla a otra
        super().__init__(padre) #llama a la clase padre a la principal
        self.controlador = controlador  #llama a los mtodos del controlador
        #self.pack() #coloca el 
        self.place(x=0, y=0, width=1100, height=650) #dimensiones que va ocupar el frame
        self.iniciar_ventana_login() #llamada  a la función de los widgets

    def conectar_db(self): #conexión base de datos
        return mysql.connector.connect( #retorna la conexión 
            host="localhost", 
            user="root", 
            password="",
            database="bd_veterinaria"
        )
    
    def iniciar_sesion(self): #función de inicio de sesión
        #obtención de los valores de los cuadros de texto
        nombre = entrada.get() 
        contrasena = entrada2.get()

        try:
            db_connection = self.conectar_db() #llamada de la conexión a la db
            cursor = db_connection.cursor() #cursor para ejecutar comandos de SQL y obtener resultados
            query = "SELECT * FROM veterinario WHERE nombre = %s AND contraseña = %s" #consulta dependiendo el usuario y contraseña 
            #%s es un cursor de posición para las variables como nnombre y contraseña
            cursor.execute(query, (nombre, contrasena)) 
            result = cursor.fetchone()#toma el resultado de la consulta

            if result: # si el resultado es que si existe ese usuario con esa contraseña 
                from menu import Menu 
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")  #cuadro de informació
                #self.destroy()
                entrada.set("")
                entrada2.set("")
                self.controlador.show_frame(Menu) #muestra el frame de menu al frente 
            else:
                messagebox.showerror("Error", "Nombre o contraseña incorrectos.")
        except Exception as e:
                messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")

        finally: #finaliza las conecciones de la db
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    
    def iniciar_ventana_login(self): #widgets
        global entrada , entrada2
        self.configure(background="#94e1b7") 
        
        tk.Label( #texto
            self,
            text="Veterinaria Perrhijos",
            background= "#94e1b7", 
            fg="#278652",
            justify="center",
            font=("Courier", 50)
        ).pack(pady=20)

        tk.Label(self, text="Nombre:", background= "#94e1b7",fg="#0C3B21",font=("Courier", 25)).place(x=350, y=150)
        entrada = tk.StringVar() 
        tk.Entry(self, textvariable=entrada, width=35).place(x=550, y=160)

        tk.Label(self, text="Contraseña:", background= "#94e1b7",fg="#0C3B21", font=("Courier", 25)).place(x=300, y=250)
        entrada2 = tk.StringVar()
        tk.Entry(self, textvariable=entrada2, show='*', width=35).place(x=550, y=260)

        #boton para iniciar sesión llama a la función
        tk.Button(self, text="Iniciar sesión", background= "#278652", fg="#DEECE4", font=("Courier", 30),command=self.iniciar_sesion).place(x=400, y=400)
       
        


    #if __name__ == "__main__":
     #   iniciar_ventana_login()


    #if __name__ == "__main__":
    #   app=Maneger()
    #  app.mainloop()

