import tkinter as tk
from tombola import Tombola
from animacion import mostrar_animacion_tombola

COLORS = {
    "background": "#4CAF50",
    "button": "#FF9800",
    "highlight": "#f44336",
    "text": "white",
    "default": "black"
}

def main():
    root = tk.Tk()
    root.title("Tombola Multijuego")
    root.geometry("1100x600")

    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    frame_contenido = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_contenido, anchor="nw")
    frame_tombolas = tk.Frame(frame_contenido)
    frame_tombolas.pack(pady=10)

    tombola_principal = Tombola(frame_tombolas, rango=(1, 40), columnas=10, max_sorteos=6, 
                                titulo="TOMBOLLA PRINCIPAL (1-40)")
    tombola_principal.marco.pack(side=tk.LEFT, padx=10)
    tombola_bono1 = Tombola(frame_tombolas, rango=(1, 12), columnas=6, max_sorteos=1, 
                            titulo="BOLA BONO 1 (1-12)")
    tombola_bono1.marco.pack(side=tk.LEFT, padx=10)
    tombola_bono2 = Tombola(frame_tombolas, rango=(1, 15), columnas=5, max_sorteos=1, 
                            titulo="BOLA BONO 2 (1-15)")
    tombola_bono2.marco.pack(side=tk.LEFT, padx=10)

    def generar_todos_en_todas():
        mostrar_animacion_tombola(root)
        root.after(1500, lambda: [tombola_principal.generar_todos(),
                                  tombola_bono1.generar_todos(),
                                  tombola_bono2.generar_todos()])

    btn_generar_todos_global = tk.Button(frame_contenido, text="Generar Todos en Todas", command=generar_todos_en_todas,
                                         font=("Arial", 12), bg=COLORS["button"], fg=COLORS["text"])
    btn_generar_todos_global.pack(pady=10)

    def reiniciar_todas():
        tombola_principal.reiniciar()
        tombola_bono1.reiniciar()
        tombola_bono2.reiniciar()

    btn_reiniciar = tk.Button(frame_contenido, text="Reiniciar Concurso", command=reiniciar_todas,
                              font=("Arial", 12), bg=COLORS["background"], fg=COLORS["text"])
    btn_reiniciar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()