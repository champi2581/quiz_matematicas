import tkinter as tk  
from tkinter import messagebox
import csv
import random

#Variablessss
nombre=""
preguntas=[]
indice=0
puntaje=0
correctas=0
incorrectas = 0
vidas=3
entrada=None
puntos_por_dificultad={1: 5, 2: 10, 3: 15}

#Ventana
ventana = tk.Tk()
ventana.title ("Quiz_Matematicas")
ventana.geometry("600x400")
ventana.configure(bg="#FFFFFF")
ventana.resizable(False,False)

#Limp
def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()

def leer_preguntas():
    lista=[]
    archivo = open (r"C:/Users/Luisito/OneDrive/Documentos/preguntas.txt",encoding="utf-8")
    lector = csv.reader (archivo)
    next(lector)
    for fila in lector:
        if len (fila) >= 3:
            lista.append(fila)
    archivo.close()
    return lista
def mostrar_inicio():
    global entrada
    limpiar()
    titulo=tk.Label(ventana, text="Quiz de Matematicas", font=("Arial",15), fg="#202020", bg="#FFFFFF")
    titulo.grid(row=0, column=0, padx=15, pady=15)
    tk.Label(ventana, text="ESCRIBE TU NOMBRE:").grid(row=1, column=0)
    entrada = tk.Entry(ventana)
    entrada.grid(row=2, column=0, pady=5)
    tk.Button(ventana, text="Empezar", command=empezar).grid(row=3, column=0, pady=5)

def empezar():
    global nombre, preguntas, indice, puntaje, correctas, incorrectas
    nombre= entrada.get().strip()
    if nombre =="":
        messagebox.showerror("Error","Escribe tu nombre")
        return
    try: 
        todas = leer_preguntas()
    except FileNotFoundError:
        messagebox.showerror("Error no se encuentra:", "C:/Users/Luisito/OneDrive/Documentos/preguntas.txt")
        return
    if len (todas)<5:
        messagebox.showerror("Error", "El archivo tiene menos de 5 preguntas")
        return
    preguntas = random.sample (todas,5)
    indice = 0
    puntaje = 0
    correctas = 0
    incorrectas = 0
    mostrar_pregunta()
#Preguntas ventana
def mostrar_pregunta():
    global entrada
    limpiar()
    fila=preguntas [indice]
    texto = fila [0]
    dificultad = fila [2]

    tk.Label (ventana, text="Pregunta " + str(indice + 1)+ " de 5").grid(row=0, column=0, pady=5)
    tk.Label (ventana, text= texto, font=("Times New Roman", 18), fg="#202020",width=30, wraplength=350).grid(row=1,column=0, pady=15)
    tk.Label (ventana, text="Dificultad:" + dificultad).grid(row=2, column=0 )
    tk.Label (ventana, text= "Puntaje:"+ str(puntaje)).grid(row=3,column=0)
    tk.Label (ventana, text= "Vidas:" + str (vidas)).grid(row=4, column=0)
    entrada = tk.Entry (ventana)
    entrada.grid(row=5, column=0, pady=10)
    tk.Button (ventana, text="Calcuar", command=calcular).grid(row=6,column=0, pady=10)

def calcular():
    try:
        respuesta=float(entrada.get())
    except ValueError:
        messagebox.showerror("Error", "Escribe solo numeros")
        return
    esperada = float(preguntas[indice][1])
    avanzar(respuesta==esperada)

def avanzar(acierto):
    global indice, puntaje, correctas, incorrectas, vidas
    dificultad = int(preguntas[indice][2])
    if acierto:
        puntaje = puntaje + puntos_por_dificultad [dificultad]
        correctas = correctas + 1
    else:
        incorrectas = incorrectas + 1
        vidas = vidas -1
    indice = indice + 1
    if vidas == 0 or indice ==5:
        mostrar_resultado()
    else:
        mostrar_pregunta()
#ventana final
def mostrar_resultado():
    limpiar()
    tk.Label  (ventana, text="Resultados de" + nombre, font=("Arial",17)).grid(row= 0, column=0, padx=20,pady=15)
    if vidas == 0:
        tk.Label(ventana, text= "¡Te quedaste sin vidas!   " \
        "Fin del juego").grid(row=6, column=0)
    tk.Label(ventana, text="Puntaje total:" + str (puntaje)).grid(row=1, column=0)
    tk.Label(ventana, text="Correctas:" + str (correctas)).grid(row=2, column=0)
    tk.Label(ventana, text="Incorrectas" + str (incorrectas)).grid(row=3, column=0)
    tk.Button(ventana, text="¿Jugar de nuevo?", command=mostrar_inicio).grid(row=4, column=0, pady=10)
    tk.Button(ventana, text="Salir", command=ventana.destroy).grid(row=5, column=0)
    messagebox.showinfo("Fin del Juego", nombre + "  tu puntaje fue: "+str(puntaje))
mostrar_inicio()
ventana.mainloop()