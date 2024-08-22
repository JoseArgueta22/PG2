import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import pygame
import threading

# Inicializar pygame para sonidos
pygame.mixer.init()

# Cargar sonido de respuesta correcta
sonido_correcto = pygame.mixer.Sound(r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Sonidos\correcto.wav")

def reproducir_sonido(sonido):
    sonido.play()

def iniciar_modulo_asociar_palabras(root):
    print("Iniciando módulo Asociar Palabras con Imágenes")

    # Limpiar la ventana actual antes de mostrar el módulo
    for widget in root.winfo_children():
        widget.destroy()

    # Lista de imágenes y respuestas correctas
    imagenes_y_respuestas = [
        (r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Imagenes\manzana.png", "manzana"),
        (r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Imagenes\banana.png", "banana"),
        # Agregar más imágenes y respuestas
    ]

    respuestas_correctas = 0
    respuestas_totales = len(imagenes_y_respuestas)
    respuesta_actual = tk.StringVar()
    indice_imagen_actual = 0

    # Crear barra de progreso
    progreso = tk.DoubleVar()
    barra_progreso = ttk.Progressbar(root, variable=progreso, maximum=respuestas_totales, length=300)
    barra_progreso.pack(pady=20)

    def cargar_imagen():
        nonlocal indice_imagen_actual
        ruta_imagen, respuesta_correcta = imagenes_y_respuestas[indice_imagen_actual]
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)
        
        # Añadir un borde negro a la imagen
        imagen_con_borde = ImageOps.expand(imagen, border=10, fill='black')
        
        imagen_tk = ImageTk.PhotoImage(imagen_con_borde)

        label_imagen.config(image=imagen_tk)
        label_imagen.image = imagen_tk
        respuesta_actual.set("")

    def verificar_respuesta():
        nonlocal respuestas_correctas, indice_imagen_actual
        if respuesta_actual.get().lower() == imagenes_y_respuestas[indice_imagen_actual][1]:
            respuestas_correctas += 1
            # Reproducir el sonido en un hilo separado
            threading.Thread(target=reproducir_sonido, args=(sonido_correcto,)).start()
            mensaje = tk.Label(root, text="+10", font=("Comic Sans MS", 40), fg="green", bg="#FFDEAD")
        else:
            mensaje = tk.Label(root, text="Incorrecto", font=("Comic Sans MS", 20), fg="red", bg="#FFDEAD")

        mensaje.pack(pady=20)

        # Actualizar la barra de progreso
        progreso.set(indice_imagen_actual + 1)

        # Eliminar el mensaje después de un breve retraso y pasar a la siguiente imagen
        root.after(1000, lambda: siguiente_imagen(mensaje))

    def siguiente_imagen(mensaje):
        nonlocal indice_imagen_actual
        mensaje.destroy()
        indice_imagen_actual += 1
        if indice_imagen_actual < respuestas_totales:
            cargar_imagen()
        else:
            tk.Label(root, text=f"Finalizado. Correctas: {respuestas_correctas}/{respuestas_totales}", font=("Comic Sans MS", 20), bg="#FFDEAD").pack(pady=20)

    # Crear la interfaz del módulo
    label_imagen = tk.Label(root, bg="#FFDEAD")
    label_imagen.pack(pady=40)
    cargar_imagen()

    entrada_respuesta = tk.Entry(root, textvariable=respuesta_actual, font=("Comic Sans MS", 14))
    entrada_respuesta.pack(pady=40)

    boton_verificar = tk.Button(root, text="Verificar", command=verificar_respuesta, font=("Comic Sans MS", 14), bg="#98FB98", fg="#008000")
    boton_verificar.pack(pady=10)

    boton_regresar = tk.Button(root, text="Regresar", command=lambda: regresar_a_principal(root), font=("Comic Sans MS", 14), bg="#FF6347", fg="white")
    boton_regresar.pack(pady=10)

def regresar_a_principal(root):
    root.destroy()
