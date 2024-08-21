from tkinter import messagebox
import winsound


# Función para iniciar una actividad
def iniciar_actividad(modulo):
    winsound.PlaySound("C:\\ruta\\a\\sonido.wav", winsound.SND_ASYNC)  # Reproduce un sonido al hacer clic
    messagebox.showinfo("Actividad", f"¡Hora de empezar el {modulo}!")

# Función para mostrar las instrucciones
def mostrar_instrucciones(instrucciones):
    messagebox.showinfo("Instrucciones", instrucciones)
