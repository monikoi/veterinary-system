import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import mysql.connector
from datetime import datetime, timedelta
from datetime import date

#clase de citas
class Citas(tk.Frame):
    #cosntructor de la clase donde el padre viene de la clase Menu
    def __init__(self, padre): 
        super().__init__(padre) 
        self.widgets() #llamada a la función de widgets
        self.mascotas() #llamda a la función de mascotas
        
    
    # Función para conectar con la base de datos
    def conectar_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_veterinaria"
        )

    #fucnión de validación  de datos, principalmente que todos los campos esten completos
    def validar_datos(self):
        global id, hour, fecha, tipo
        #obtiene los valores de las lista desplegabes, calendario..
        id = li_mascota.get()
        hour = opc_hora.get()
        fecha = cal.get_date()
        tipo = var2.get()

        if not id or not hour or not fecha:
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return False
        return True
    
    #función de validación de fecha, la cual revisa que no se selecciones ninguna fecha anterior a la actual
    def validar_fecha (self):
        fecha = cal.get_date() #obención de fecha del calendario
        fecha_actual = date.today() #obtención de fecha de la computadora
        #Obtebción de fecha en el formato correcto
        fecha = datetime.strptime(fecha, '%m/%d/%y').date() #casteo de formato correcto de la fecha 
        fecha = fecha.strftime('%Y-%m-%d')
        fecha_actual = fecha_actual.strftime('%Y-%m-%d') #casteo de formato correcto de la fecha 
        print(fecha_actual)
        print(fecha)
        if( fecha > fecha_actual) : return True #condiconal de que fecha seleccionada sea mayor a la fecha actual
        else :
            messagebox.showerror("Error", "Ingresa una fecha correcta.")
            return False

    #fucnión de registro de consulta 
    def registrar(self):
        if self.validar_datos() and self.validar_fecha(): #condiconal que llama a las fucniones de validación de datos y validar fecha
            #si alguna de estas retorna False  no continua con el registro de la consulta
            try:
                hora = f"{hour}:00" #agrega a hora el forma igual de la base de datos 1:00:00
                fecha = cal.get_date()  #obención de fecha del calendario y casteo al formato de la bas de datos año-mes-dia
                fecha = datetime.strptime(fecha, '%m/%d/%y').strftime('%Y-%m-%d')
                print(fecha)
                mascotaId="" #como en la lista de opciones de mascota el nombre y id de mascota estan pegados, de acuerdo a esa oppción que se elija 
                #se recorre la cadena obtenida de la opción y cuando encuentre numeros los concatena para obtener el ID 
                for i in id:
                    for x in range(0,10):
                        if i == str(x):
                            mascotaId += i

                print (mascotaId)

                db = self.conectar_db()  # Establecer la conexión con la base de datos
                cursor = db.cursor()
                query = "SELECT Nombre FROM mascota WHERE (ID) = %s" #hace la selección de datos de la mascota para imprimirlos en un mesaje de 
                #de información y confirmación de registro
                cursor.execute(query, (int(mascotaId),))
                resultado = cursor.fetchone()
                #print(resultado[0])
                mensaje= "Nombre : "+ str(resultado[0]) + "  ID: "+ mascotaId +"\n hora: "+ str(hora)+"\n fecha: "+ str(fecha)
               # print(mensaje)
                respuesta = messagebox.askyesno("¿Estás seguro de registrar? ", mensaje)
            
                #si, si se desea continuar con el registro entra al if donde se hace el insert con los valores
                if respuesta:
                    query = "INSERT INTO consultas (Fecha, Hora, Tipo,MascotaId) VALUES (%s, %s, %s, %s)"
                    cursor.execute(query, (fecha, hora, tipo, int(mascotaId)))
                    db.commit()

                    messagebox.showinfo("Éxito", "Consulta registrada correctamente.")
                    self.vaciar_datos()
                    db.close()
            except TypeError as e:
                messagebox.showerror("Error", "La mascota puede no estar registrada.")
            except ValueError:
                messagebox.showerror("Error", "Revisa que los datos sean correctos\n Y que todos los campos esten completos")

    #fucnión de selección de fecha 
    def seleccionar_fecha(self, event):
        horas_disponibles=['10:00', '11:00', '12:00', '01:00', '03:00', '04:00', '05:00', '06:00']
        fecha = cal.get_date()
        fecha = datetime.strptime(fecha, '%m/%d/%y').strftime('%Y-%m-%d')
        #print(fecha)
        try:
            db = self.conectar_db()  # Establecer la conexión con la base de datos
            cursor = db.cursor()
            query = "SELECT Hora FROM consultas WHERE (Fecha) = %s"
            cursor.execute(query, (fecha,))
            resultado = cursor.fetchall() 
            
            #print(resultado)
           
            if resultado:
                #print("nio entra")
                horas = []
                horas = [(datetime.min + fila[0]).strftime('%H:%M') for fila in resultado]
                #se usa para formatear una fecha u hora
                print(horas)
                horas_disponibles = [x for x in horas_disponibles if x not in horas]
                #print("yatermino esto")
                opcion=tk.OptionMenu(self, opc_hora,*horas_disponibles)
                opcion.config(width=50)
                opcion.pack(padx=30, pady=30)
                opcion.place(x=500, y=150)

            else:
                opcion=tk.OptionMenu(self, opc_hora,*horas_disponibles)
                opcion.config(width=50)
                opcion.pack(padx=30, pady=30)
                opcion.place(x=500, y=150)

            db.close()
        except TypeError as e:
            messagebox.showerror("Error")
            #print(e)
        except ValueError:
            messagebox.showerror("Error", "ocurrio un error\n revisa que los datos sean correctos")

    #fucnión que llena la lista de opciones de mascotas con su id y nombre
    def mascotas (self):
        global opc_mascota
        mascota=[]
        try:
            db = self.conectar_db()  # Establecer la conexión con la base de datos
            cursor = db.cursor()
            query = "SELECT Nombre, ID FROM mascota"
            cursor.execute(query)
            resultado = cursor.fetchall()
            db.close()
            for nombre, id_ in resultado:
                opc = f"{nombre} (ID: {id_})"  # Concatenación adecuada y legible
                mascota.append(opc)

            opc_mascota=tk.OptionMenu(self, li_mascota,*mascota)
            opc_mascota.config(width=50)
            opc_mascota.pack(padx=30, pady=30)
            opc_mascota.place(x=500, y=250)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", "conexión en la base")

    #función de limpiar widgets
    def vaciar_datos(self):
        var2.set("Tipo de cita")
        li_mascota.set("Mascotas")
        opc_hora.set("Hora")

    #función de widgets 
    def widgets(self):
        global cal, opc_hora, var2, opcion, li_mascota

        cal = Calendar(self, selectmode= 'day', year=2025 , month= 5, dat = 16)
        cal.config(background="#8acca8")  # Color de fondo del calendario
        cal.config(foreground="#ffffff")  # Color del texto (días) en el calendario
        cal.config(selectbackground="#2E8B57")  # Color de fondo al seleccionar una fecha
        cal.config(selectforeground="white") #Color del texto de la fecha seleccionada
        cal.place(x=20, y=90, width=450, height=350)
        cal.bind("<<CalendarSelected>>", self.seleccionar_fecha)

        #lista desplegable para las horas
        opc_hora = tk.StringVar(self)
        opc_hora.set('Hora')
        
        #Datos de mascota
        label1 = Label(self, text="Datos de la mascota", background="#aeebc9",fg="#0C3B21",font=("Courier", 15))
        label1.place(x=500, y=200, height=40, width=300)
        #btn_nombre= Button(self, text='Buscar', command=self.buscar_nombre).place(x= 800, y=250)
        li_mascota = tk.StringVar(self)
        li_mascota.set('Mascotas')
        

        #tipo de cita
        var2 = tk.StringVar(self)
        var2.set('Tipo de Cita')
        tipo=['Revición general', 'Vacunación', 'Estilista']
        opcion=tk.OptionMenu(self, var2,*tipo)
        opcion.config(width=50)
        opcion.pack(padx=30, pady=30)
        opcion.place(x=500, y=350)

        #botones
        btn_registrar= Button(self, text='Registrar Consulta', command=self.registrar, font=("Times New Roman",20),bg="#a9efc8").place(x= 550, y=400)





    
