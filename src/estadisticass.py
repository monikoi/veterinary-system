from tkinter import *
import tkinter as tk
import mysql.connector
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Clase Principal que extiende de Frame para implementar interfaz
class Estadistica_mensual(tk.Frame):

    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()

    #Funcion para conectar la base de datos
    def conectar_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_veterinaria"
        )

    # Funcion principal
    def cargar_estadisticas(self):
        conn = self.conectar_db() #Se guarda la conexion con la base de datos
        #cursor = db.cursor()
        #conn = sqlite3.connect('bd_veterinaria.db')
        df_mascotas = pd.read_sql_query("SELECT * FROM mascota", conn)  #Guarda todos los datos de la tabla de mascota
        df_consultas = pd.read_sql_query("SELECT * FROM consultas", conn) #guarda todos los datos de la tabla de consultas
        conn.close() #Cierra la conexion

        df_mascotas['FechaRegistro'] = pd.to_datetime(df_mascotas['FechaRegistro']) 
        df_consultas['Fecha'] = pd.to_datetime(df_consultas['Fecha'])

        #Estadisticas
        total_mascotas = len(df_mascotas) #cuenta las maascotas
        total_citas = len(df_consultas) #cuenta las citas
        tipo_comun = df_consultas['Tipo'].value_counts().idxmax() #obtiene el tipo de cita mas comun

        # Mostrar datos numéricos
        lbl_total_mascotas.config(text=f"Total de mascotas: {total_mascotas}") #Se imprimen en lbl los datos
        lbl_total_citas.config(text=f"Total de citas: {total_citas}")
        lbl_tipo_comun.config(text=f"Tipo de cita más común: {tipo_comun}")

        # Top 3 mascotas con más citas
        ultimo_anio = datetime.now().year - 1  #Obtiene el año actual y le resta un año
        consultas_ultimo_anio = df_consultas[df_consultas['Fecha'].dt.year >= ultimo_anio] #guarda los que tienen fechas e maximo un año atras
        top_3 = consultas_ultimo_anio['MascotaId'].value_counts().head(3) #Cuenta cuales se repiten y cuales son las tres mas altas
        texto_top3 = ""

        #Recorre el top 3 con enumeracioness (i es el numero de orden, empezando desde el 1)
        for i, (id_mascota, cantidad) in enumerate(top_3.items(), 1): 
            #Busca el nombre de la mascota correspondiente al Id_Mascota en el Dataframe df_mascotas
            nombre = df_mascotas[df_mascotas['ID'] == id_mascota]['Nombre'].values[0]
            #Agrega al texto el nombre y la cantidad de citas de la mascota, con formato
            texto_top3 += f"{i}. {nombre} ({cantidad} citas)\n"
        #Muestra el texto generado en una etiqueta label
        lbl_top3.config(text=texto_top3)

        # Total de visitas por tipo de mascota

        #Une (merge) los dateframes df_consulta y df_mascotas 
        df_merged = pd.merge(df_consultas, df_mascotas, left_on='MascotaId', right_on='ID')

        #Agrupa los datos por stipo de mascota (columna 'Tipo_y') y cuenta cuantas consultas hay por cada uno
        total_visitas = df_merged.groupby('Tipo_y')['MascotaId'].count()

        #convierte los resultados a una lista y luego los inserta en la tabla
        tabla = total_visitas.reset_index().values.tolist()
        
        # Limpiar la tabla actual del TreeView
        #Recorre todas las filas de la tabla y los eliminas
        for row in tabla_tree.get_children():
            tabla_tree.delete(row)
        #Inserta los nuevos datos en la tabla
        for tipo, total in tabla:
            tabla_tree.insert('', 'end', values=(tipo, total))

        # Gráfica: mascotas por especie ciculo
        #Crea una figura 3x3 pulgadas
        fig1 = plt.Figure(figsize=(3, 3))
        #Añade un subplot (area de dibujo) a la figura
        ax1 = fig1.add_subplot(111)
        #Cuenta cuantas mascotas hay  de cada tipo y crea un grafico circular
        df_mascotas['Tipo'].value_counts().plot.pie(ax=ax1, autopct='%1.1f%%', title='Mascotas por Especie')
        #Llama a una funcion para mostrar la grafica de la interfaz
        self.mostrar_grafica(fig1, frame_graf1)


        # Gráfica: nuevas mascotas por mes
        #Crea una figura 3x3 pulgadas
        fig3 = plt.Figure(figsize=(3, 3))
        #Añade un subplot (area de dibujo) a la figura
        ax3 = fig3.add_subplot(111)
        #Agrupa las mascotas por mes de registro y cuenta cuantas se han registrado en cada mes
        nuevas_por_mes = df_mascotas.groupby(df_mascotas['FechaRegistro'].dt.to_period("M")).count()['ID']
        #Dibuja un grafico de barras con los datos anteriores
        nuevas_por_mes.plot(kind='bar', ax=ax3)

        #Configura el titulo y etiquetaas de los ejes
        ax3.set_title("Mascotas Nuevas por Mes")
        ax3.set_xlabel("Mes")
        ax3.set_ylabel("Cantidad")

        #Ajusta el diseño para que no se sobrepongan los elementos
        fig3.tight_layout()
        #Muestra la grafifica en la interfaz
        self.mostrar_grafica(fig3, frame_graf3)

    #Mostrar una gráfica en un frame
    def mostrar_grafica(self,figura, contenedor):
        for widget in contenedor.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(figura, master=contenedor)
        canvas.draw()
        canvas.get_tk_widget().pack()


#Carga los componentes que tendra el frame
    def widgets(self):
        global lbl_total_mascotas, lbl_total_citas,lbl_tipo_comun,lbl_top3_title,lbl_top3,tabla_tree,frame_graf1,frame_graf3
        

        # Datos numéricos, diseño de las fuentes de los labels 
        lbl_total_mascotas = tk.Label(self, text="", font=("Arial", 12), background="#f5f5dc")
        lbl_total_mascotas.pack()

        lbl_total_citas = tk.Label(self, text="", font=("Arial", 12),background="#f5f5dc")
        lbl_total_citas.pack()

        lbl_tipo_comun = tk.Label(self, text="", font=("Arial", 12), background="#f5f5dc")
        lbl_tipo_comun.pack()

        lbl_top3_title = tk.Label(self, text="Top 3 mascotas con más citas (último año):", font=("Arial", 12, "bold"),  background="#f5f5dc")
        lbl_top3_title.pack()

        lbl_top3 = tk.Label(self, text="", font=("Arial", 10), justify="left",  background="#f5f5dc")
        lbl_top3.pack()

        #  Muestra las etiquetas del  total de citas por tipo de mascota 
        tk.Label(self, text="Total de citas por tipo de mascota:", font=("Arial", 12, "bold"),  background="#f5f5dc").pack()
        tabla_tree = ttk.Treeview(self, columns=("Tipo", "Total"), show="headings", height=3)
        tabla_tree.heading("Tipo", text="Tipo")
        tabla_tree.heading("Total", text="Total de Visitas")
        tabla_tree.pack(pady=5)

        # Frames para gráficas
        frame_graf1 = tk.Frame(self)
        frame_graf1.pack(pady=5)
        frame_graf1.place(x=50, y=320)
        frame_graf3 = tk.Frame(self)
        frame_graf3.pack(pady=5)
        frame_graf3.place(x=550, y=320)

        # Botón de cargar estadisticas
        tk.Button(self, text=" Cargar Estadísticas",  background="#0C3B21",  fg="#DEECE4", command=self.cargar_estadisticas).pack(pady=10) 