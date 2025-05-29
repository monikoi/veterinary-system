from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox

class Cancelar(tk.Frame):

    def __init__(self, padre): #clase de cancelaciones que tiene como padre a menu
        super().__init__(padre)
        self.widgets() #llamada a los widgets
        self.llenar_tabla() #llamada a fución de llenar tabla
        
    
    #conección a la db
    def conectar_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_veterinaria"
        )


    #función de obtención de consultas para llenar la tabla de consultas
    def obtener_consultas(self):
        db = self.conectar_db()
        cursor = db.cursor()
        query = """
        SELECT consultas.ID, consultas.Fecha, consultas.Hora, consultas.Tipo, mascota.Nombre
        FROM consultas
        JOIN mascota ON consultas.MascotaId = mascota.ID;
        """
        cursor.execute(query)
        consultas = cursor.fetchall()  # Obtener todos los resultados
        db.close()
        return consultas
    
    def verificar_eliminacion(self):
        lista = tabla.selection()
        if not lista:
            messagebox.showerror("Error", "Seleccione una dato de la tabla.")
            return
        else:
            #messagebox.showerror("Correcto")
            valores = tabla.item(lista, "values")
            #print(valores)
            self.eliminar(valores)
       
    
    #funcion de eliminación de eliminación 
    def eliminar(self, datos):

        try:
            id=int(datos[0])
            print(id)
            db = self.conectar_db()
            cursor = db.cursor()
            query = "DELETE FROM consultas WHERE ID = %s LIMIT 1"
            cursor.execute(query, (id,))
            db.commit()
            messagebox.showinfo("Exito", "La cita fue cancelada exitosamente")
            db.close
            self.llenar_tabla() #llamada a la función que limpia y vuelve a cargar la tabla ya actualizada
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "no se pudeo cancelar la cita")
            #print(f"Error eliminando: {e}")


#función de llenar taabla se encarga primero de eliminar los datos anteriores por posibles sobreescrituras
    def llenar_tabla(self):
        for item in tabla.get_children():
            tabla.delete(item)

        consultas = self.obtener_consultas() #llamada de obtención de consultas
        for consulta in consultas: #recorre la tupla de datos retornado de obtner consultas
            tabla.insert("", "end", values=consulta)  # "" -> se refere a insertar desde el inicio
            # 


    def widgets(self):
        global tabla
        label= Label(self, text = "CANCELACIONES ", font=("Arial", 35), background="#DED1C1")
        label.place(x=50, y=20,  width=800)
        tabla = ttk.Treeview(self, columns=("ID", "Fecha", "Hora", "Tipo", "Nombre"), show="headings")
        tabla.place(x=50, y=100,  width=800)

        #Define el estilo de la tabla 
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

        # Definir los encabezados de las columnas
        tabla.heading("ID", text="ID")
        tabla.heading("Fecha", text="Fecha")
        tabla.heading("Hora", text="Hora")
        tabla.heading("Tipo", text="Tipo")
        tabla.heading("Nombre", text="Nombre")

        tabla.column("ID", width=50, anchor="center")
        tabla.column("Fecha", width=70, anchor="center")
        tabla.column("Hora", width=50, anchor="center")
        tabla.column("Tipo", width=70, anchor="center")
        for item in tabla.get_children(): # se usa get_children que retorna todos los elementos dentro de la tabla para limpiarla
            tabla.delete(item)

        btn= Button(self, text='Eliminar',font=("Times New Roman",20),bg="#a9efc8", command=self.verificar_eliminacion).place(x= 400, y=400, width=150, height=70)
        #btn= Button(self, text='Actualizar',font=("Times New Roman",15),bg="#a9efc8", command=self.llenar_tabla).place(x= 200, y=400, width=150, height=100)



    


        