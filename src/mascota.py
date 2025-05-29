from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from datetime import datetime

class Registros_M(tk.Frame):

    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()
        self.llenar_mascotas()
    
      # Función para conectar con la base de datos
    def conectar_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_veterinaria"
        )

    #función de registro de mascota
    def registrar_mascota (self):
        nombre = nTxt.get()
        dueno= dTxt.get()
        tipo= varT.get()
        raza = rTxt.get()
        edad = eTxt.get()
        fecha = datetime.now().date()  #
        if not nombre or not edad or not dueno or not tipo or not raza :
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
        elif int(edad)>20 | int(edad)<0 : 
            messagebox.showerror("Error", "La edad esta fuera del rango")
        else:
            try :
                db = self.conectar_db()
                cursor = db.cursor()
                query = "INSERT INTO mascota (Nombre, Dueño, Tipo, Raza, Edad, FechaRegistro) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nombre, dueno, tipo, raza, int(edad), fecha))
                db.commit()
                messagebox.showinfo("Éxito", "Mascota registrada exitosamente.")
                db.close()
                self.llenar_mascotas()
                self.vaciar_datos()

            except mysql.connector.Error as e:
                messagebox.showerror("Error", "No se puede registrar la mascota en este momento")

            except TypeError as e:
                messagebox.showerror("Error", "ocurrio un error\n revisa que los datos sean correctos")
            except ValueError:
                messagebox.showerror("Error", "ocurrio un error\n revisa que los datos sean correctos")

        
    def llenar_mascotas(self):
        try :
            db = self.conectar_db()
            cursor = db.cursor()
            query = "SELECT Nombre, ID from mascota"
            cursor.execute(query)
            resultado=cursor.fetchall()
            
            for item in tabla.get_children():
                tabla.delete(item)

            for consulta in resultado: #recorre la tupla de datos retornado de obtner consultas
                tabla.insert("", "end", values=consulta)  # "" -> se refere a insertar desde el inicio
            #
            db.close()
        except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Error", "Conexión de datos")

    #función que limpia los cuadros de texto
    def vaciar_datos(self):
        nTxt.delete(0, tk.END)
        eTxt.delete(0, tk.END)
        dTxt.delete(0, tk.END)
        rTxt.delete(0, tk.END)
        varT.set("Tipo de Animal")

    #función de widgets
    def widgets(self):
        global nTxt, eTxt, rTxt, dTxt, varT, tabla
        nombre = Label(self, text="Nombre:")
        nombre.pack()
        nombre.config(bg="#D2B48C", fg="black", font=("Arial", 15))
        nombre.place(x=100, y=90)
        nTxt = Entry(self)
        nTxt.place(x=200, y=90, width=200)
        edad = Label(self, text="Edad:")
        edad.pack()
        edad.config(bg="#D2B48C", fg="black", font=("Arial", 15))
        edad.place(x=100, y=140)
        eTxt = Entry(self)
        eTxt.place(x=200, y=140, width=200)

        varT = tk.StringVar(self)
        varT.set('Tipo de Animal')
        tipo=['Perro', 'Gato', 'Ave', 'Otros']
        opcion=tk.OptionMenu(self, varT,*tipo)
        opcion.config(width=50, background="#D2B48C")
        opcion.pack(padx=30, pady=30)
        opcion.place(x=150, y=190)


        raza = Label(self, text="Raza:")
        raza.pack()
        raza.config(bg="#D2B48C", fg="black", font=("Arial", 15))
        raza.place(x=100, y=240)
        rTxt = Entry(self)
        rTxt.place(x=200, y=240, width=200)
        dueno = Label(self, text="Dueño:")
        dueno.pack()
        dueno.config(bg="#D2B48C", fg="black", font=("Arial", 15))
        dueno.place(x=100, y=290)
        dTxt = Entry(self)
        dTxt.place(x=200, y=290, width=200)
        btn1 = tk.Button(self, text="Registrar", bg="#98e7b1",fg="white",font=("Courier", 25), command=self.registrar_mascota)  #command=registrar
        btn1.place(x=150, y=350)

        style = ttk.Style()
        style.theme_use("default")  # Asegura que el estilo se aplique

        style.configure("Treeview",
            background="#DED1C1",    # Color del fondo de filas
            foreground="black",      # Color del texto
            rowheight=25
        )
        style.configure("Treeview.Heading",
            background="#D2B48C",   # Color de fondo del encabezado
            foreground="white",     # Color del texto del encabezado
            font=('Arial', 10, 'bold')
        )

        #Tabla de mascotas
        tabla = ttk.Treeview(self, columns=("ID", "Nombre"), show="headings")
        tabla.place(x=650, y=80,  width=200)
        
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("ID", text="ID")
        
        tabla.column("Nombre", width=20, anchor="center")
        tabla.column("ID", width=20, anchor="center")
        
    

  