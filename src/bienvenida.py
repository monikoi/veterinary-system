from tkinter import *
from tkinter import ttk
import tkinter as tk


class Bienvenida(tk.Frame):
   def __init__(self, padre):
        super().__init__(padre)
        self.widgets()
    
    def widgets(self):
        bien = Label(text="BIENVENIDO", font=("Arial", 50), bg="#D2B48C", fg="#2271b3")
        bien.pack()
        bien.place(x=100, y=50)
        

    