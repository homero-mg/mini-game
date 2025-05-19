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

def mostrar_pregunta(nombre_jugador):
    #Creo una nueva ventana
    ventana_pregunta = tk.Tk()
    ventana_pregunta.title('Pregunta 1')
    ventana_pregunta.geometry("500x300")
    #Creo la pregunta y las respuestas en una variable y un diccionario
    pregunta = '¿Cuál es la capital de Portugal?'
    opciones = {
        'A' : 'Madrid',
        'B' : 'Lisboa', # Esta es la correcta
        'C' : 'Dublin'
    }
    respuesta_correcta = 'B'

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?', (nombre_jugador,))
            conn.commit()

    # Vamos a mostrar la pregunta 
    tk.Label(ventana_pregunta, text=pregunta, font=('Arial', 14)).pack(pady=20)

    # Vamos a mostrar los botones        
    for clave, valor in opciones.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana_pregunta, text=texto, width=20, command=lambda: responder(clave)).pack(pady=5)
    
       
#--------------------------------------
def mostrar_pregunta2(nombre_jugador):
    #Creo una nueva ventana
    ventana_pregunta2 = tk.Tk()
    ventana_pregunta2.title('Pregunta 1')
    ventana_pregunta2.geometry("500x300")
    #Creo la pregunta y las respuestas en una variable y un diccionario
    pregunta2 = '¿Cuanto es 2 + 2?'
    opciones2 = {
        'A' : '1',
        'B' : '4', # Esta es la correcta
        'C' : '6'
    }
    respuesta_correcta2 = 'B'

    def responder2(eleccion):
        if eleccion == respuesta_correcta2:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?', (nombre_jugador,))
            conn.commit()

    # Vamos a mostrar la pregunta 
    tk.Label(ventana_pregunta2, text=pregunta2, font=('Arial', 14)).pack(pady=20)

    # Vamos a mostrar los botones        
    for clave, valor in opciones2.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana_pregunta2, text=texto, width=20, command=lambda: responder2(clave)).pack(pady=5)







#-----------------------------------------
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
        #destruyo las ventana principal
        root.destroy()
        # llamo a otra funcion de preguntas
        mostrar_pregunta(nombre)
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