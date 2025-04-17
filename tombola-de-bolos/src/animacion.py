import tkinter as tk
from bola import Bola

def animar_bolas_erraticas(canvas, bolas, delay):
    for bola in bolas:
        bola.mover()
    canvas.after(delay, animar_bolas_erraticas, canvas, bolas, delay)

def mostrar_animacion_tombola(root):
    ventana_animacion = tk.Toplevel(root)
    ventana_animacion.title("Tómbola con Bolas Erráticas")
    ventana_animacion.geometry("400x400")
    canvas = tk.Canvas(ventana_animacion, width=400, height=400, bg="white")
    canvas.pack()
    canvas.create_oval(50, 50, 350, 350, outline="black", width=2)
    centro_x, centro_y = 200, 200
    radio_area = 150
    num_bolas = 40
    delay = 50
    bolas = [Bola(canvas, centro_x, centro_y, radio_area) for _ in range(num_bolas)]
    animar_bolas_erraticas(canvas, bolas, delay)
    delay = 5000
    canvas.after(delay, lambda: ventana_animacion.destroy())