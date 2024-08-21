import tkinter as tk
from PIL import Image, ImageTk
import pygame
import time

# Inicializar pygame para sonidos
pygame.mixer.init()

# Cargar sonido de respuesta correcta
sonido_correcto = pygame.mixer.Sound(r"C:\Users\acer\Desktop\Cosas U\10mo semestre\PG2\Sonidos\correcto.wav")

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

    def cargar_imagen():
        nonlocal indice_imagen_actual
        ruta_imagen, respuesta_correcta = imagenes_y_respuestas[indice_imagen_actual]
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label_imagen.config(image=imagen_tk)
        label_imagen.image = imagen_tk
        respuesta_actual.set("")

    def verificar_respuesta():
        nonlocal respuestas_correctas, indice_imagen_actual
        if respuesta_actual.get().lower() == imagenes_y_respuestas[indice_imagen_actual][1]:
            respuestas_correctas += 1
            sonido_correcto.play()
            tk.Label(root, text="+10", font=("Comic Sans MS", 40), fg="green", bg="#FFDEAD").pack()
            time.sleep(1)
        else:
            tk.Label(root, text="Incorrecto", font=("Comic Sans MS", 20), fg="red", bg="#FFDEAD").pack()
            time.sleep(1)

        indice_imagen_actual += 1
        if indice_imagen_actual < respuestas_totales:
            cargar_imagen()
        else:
            tk.Label(root, text=f"Finalizado. Correctas: {respuestas_correctas}/{respuestas_totales}", font=("Comic Sans MS", 20), bg="#FFDEAD").pack()

    # Crear la interfaz del módulo
    label_imagen = tk.Label(root, bg="#FFDEAD")
    label_imagen.pack(pady=20)
    cargar_imagen()

    entrada_respuesta = tk.Entry(root, textvariable=respuesta_actual, font=("Comic Sans MS", 14))
    entrada_respuesta.pack(pady=10)

    boton_verificar = tk.Button(root, text="Verificar", command=verificar_respuesta, font=("Comic Sans MS", 14), bg="#98FB98", fg="#008000")
    boton_verificar.pack(pady=10)

    boton_regresar = tk.Button(root, text="Regresar", command=lambda: regresar_a_principal(root), font=("Comic Sans MS", 14), bg="#FF6347", fg="white")
    boton_regresar.pack(pady=10)

def regresar_a_principal(root):
    # Cierra el módulo actual y regresa a la interfaz principal
    root.destroy()
    