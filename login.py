import tkinter as tk
import sqlite3

#Creación/conexion de la base de datos
conn = sqlite3.connect('jugadores.db')

# Creo cursor
cursor = conn.cursor()

# Crear tabla para almacenar datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS jugadores (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               puntuacion INTERGER DEFAULT 0
               )
''')

#Confirmo esa creacion de tabla
conn.commit()

# Creo funcion apra comenzar el juego
def comenzar_juego():
    #Almaceno el nombre del cuadro de entrada en una variable
    nombre = entrada_nombre.get().strip()
    # creo condicional para forzar la entrada de nombre
    if nombre:
        #si existe lo almaceno en la bbdd
        cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?, ?)", (nombre, 0))
        #confirmo cambios
        conn.commit()
        # Aqui iria lallamada a la siguiente ventana
    else:
        label_mensaje.config(text='Por favor, ingresa un nombre!')

# Creacion de la ventana principal
root = tk.Tk()
root.title('Login del juego')
root.geometry('300x250')

# Widgets
# Texto
label_titulo = tk.Label(root, text='Introduce tu nombre', font= ("Modern", 20))
label_titulo.pack(pady=20)

# Cuadro de Entrada de texto
entrada_nombre = tk.Entry(root, font= ("Modern", 14))
entrada_nombre.pack(pady=10)

# Boton para iniciar el juego
boton_comenzar = tk.Button(root, text='COMENZAR', font=("Modern", 14), command=comenzar_juego)
boton_comenzar.pack(pady=10)

# Creo un label para informar de que no se ha introducido un nombre
label_mensaje = tk.Label(root, text='', fg='red', font=("Modern", 14))
label_mensaje.pack(pady=10)

#Mantengo la ventana abierta
root.mainloop()

# Cirroconexion con bbdd
conn.close()