import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import winsound
from funciones import iniciar_actividad, mostrar_instrucciones
from modulo_asociar_palabras import iniciar_modulo_asociar_palabras

def iniciar_actividad(modulo):
    print(f"Actividad iniciada: {modulo}")
    if modulo == "Módulo 1":
        iniciar_modulo_asociar_palabras(root)  # Pasar la ventana principal
    else:
        winsound.PlaySound("C:\\Users\\acer\\Desktop\\Cosas U\\10mo semestre\\PG2\\Sonidos\\sonido_mario.wav", winsound.SND_ASYNC)
        messagebox.showinfo("Actividad", f"¡Hora de empezar el {modulo}!")

# Función para aplicar el efecto de zoom al pasar el mouse sobre un botón
def on_enter(event):
    event.widget.config(font=("Comic Sans MS", 16))

# Función para quitar el efecto de zoom cuando el mouse sale del botón
def on_leave(event):
    event.widget.config(font=("Comic Sans MS", 14))

# Función para animar las letras del título
def animar_titulo(titulo_label, texto, indice=0):
    colores = ["#FF4500", "#FF6347", "#FFD700", "#ADFF2F", "#00CED1", "#1E90FF", "#DA70D6"]
    
    if indice < len(texto):
        titulo_label.config(text=texto[:indice+1], fg=random.choice(colores))
        titulo_label.after(100, animar_titulo, titulo_label, texto, indice + 1)
    else:
        titulo_label.after(1000, lambda: animar_titulo(titulo_label, texto))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Plataforma Web para la estimulación y aprendizaje de palabras")

# Configura la ventana para que esté en pantalla completa
root.attributes("-fullscreen", True)
root.configure(bg="#FFDEAD")

# Función para cargar y mostrar la imagen de la tuerca
def cargar_imagen_tuerca():
    ruta_tuerca = r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Imagenes\tuerca.png"
    imagen_tuerca = Image.open(ruta_tuerca)
    imagen_tuerca = imagen_tuerca.resize((70, 40), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(imagen_tuerca)

imagen_tuerca_tk = cargar_imagen_tuerca()
label_tuerca = tk.Label(root, image=imagen_tuerca_tk, bg="#FFDEAD", borderwidth=2, relief="solid")
label_tuerca.grid(row=0, column=2, padx=20, pady=10, sticky='ne')

# Título Principal
titulo_texto = "¡Bienvenido a Tu Aventura de Aprendizaje!"
titulo = tk.Label(root, font=("Comic Sans MS", 24, "bold"), bg="#FFDEAD")
titulo.grid(row=0, column=1, padx=30, pady=10, sticky='n')

# Segundo Título
subtitulo_texto = "Plataforma Web para la estimulación y aprendizaje de palabras"
subtitulo = tk.Label(root, font=("Comic Sans MS", 18, "bold"), bg="#FFDEAD")
subtitulo.grid(row=1, column=1, padx=30, pady=10, sticky='n')

# Iniciar animación de títulos
animar_titulo(titulo, titulo_texto)
animar_titulo(subtitulo, subtitulo_texto)

# Función para cargar una imagen y crear un módulo
def crear_modulo(contenedor, ruta_imagen, texto_boton, modulo, columna, instrucciones, tamano_boton=(30, 2)):
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    label_imagen = tk.Label(contenedor, image=imagen_tk, bg="#FFDEAD", borderwidth=5, relief="solid")
    label_imagen.image = imagen_tk  # Mantener una referencia de la imagen para evitar que sea recolectada por el GC
    label_imagen.grid(row=0, column=columna, padx=60, pady=50)

    boton_modulo = tk.Button(contenedor, text=texto_boton, font=("Comic Sans MS", 14), bg="#98FB98", fg="#008000", width=tamano_boton[0], height=tamano_boton[1], command=lambda: iniciar_actividad(modulo), borderwidth=3, relief="solid")
    boton_modulo.grid(row=1, column=columna, padx=60, pady=20)
    
    boton_modulo.bind("<Enter>", on_enter)
    boton_modulo.bind("<Leave>", on_leave)

    # Botón de instrucciones
    boton_instrucciones = tk.Button(contenedor, text=f"Instrucciones {modulo}", font=("Comic Sans MS", 14), bg="#FFD700", fg="#000000", command=lambda: mostrar_instrucciones(instrucciones), borderwidth=3, relief="solid")
    boton_instrucciones.grid(row=2, column=columna, padx=60, pady=10)

# Crear contenedor para los módulos
contenedor = tk.Frame(root, bg="#FFDEAD")
contenedor.grid(row=2, column=0, columnspan=3, pady=40)

# Crear módulos con sus respectivas imágenes, botones y instrucciones en una fila horizontal
crear_modulo(contenedor, r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Imagenes\lapiz.jpg", "Módulo 1: Asociar Palabras con Imagen", "Módulo 1", 0, "Instrucciones para el Módulo 1")
crear_modulo(contenedor, r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Imagenes\oracion.jpg", "Módulo 2: Completar Oraciones", "Módulo 2", 1, "Instrucciones para el Módulo 2")
crear_modulo(contenedor, r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Imagenes\repetir.png", "Módulo 3: Repetir Palabras", "Módulo 3", 2, "Instrucciones para el Módulo 3")

# Función para regresar (cerrar la ventana actual)
def regresar():
    root.destroy()

# Crear botón de "Regresar" en la parte inferior izquierda
boton_regresar = tk.Button(root, text="Salir", font=("Comic Sans MS", 14), bg="#FF6347", fg="white", command=regresar, borderwidth=3, relief="solid")
boton_regresar.place(relx=0.02, rely=0.9)

# Ejecución de la ventana principal
root.mainloop()
