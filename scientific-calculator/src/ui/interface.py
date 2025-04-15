import tkinter as tk
from tkinter import messagebox
import math

class CalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator
        self.master = tk.Tk()  # Crear la ventana principal de Tkinter
        self.master.title("Calculadora Científica")
        self.master.geometry("500x700")  # Tamaño fijo de la ventana
        self.master.resizable(False, False)  # Deshabilitar redimensionamiento
        self.result_var = tk.StringVar()  # Inicializar la variable para el resultado
        self.create_widgets()

    def create_widgets(self):
        """Crea los widgets de la interfaz gráfica."""
        # Campo de entrada para mostrar la expresión y el resultado
        self.display = tk.Entry(self.master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # Botones de la calculadora
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^', 'sin',
            'cos', 'tan', '(', ')'
        ]

        # Colores para los botones
        button_colors = {
            'numbers': "#f0f0f0",  # Gris claro para números
            'operators': "#ffcccb",  # Rojo claro para operadores
            'functions': "#d1e7dd",  # Verde claro para funciones
            'clear': "#f8d7da",  # Rosa claro para el botón C
            'equals': "#cfe2ff"  # Azul claro para el botón =
        }

        row_val = 1
        col_val = 0

        for button_text in button_texts:
            if button_text.isdigit() or button_text == '.':
                color = button_colors['numbers']
            elif button_text in ['+', '-', '*', '/', '^']:
                color = button_colors['operators']
            elif button_text in ['sin', 'cos', 'tan', '√', '(', ')']:
                color = button_colors['functions']
            elif button_text == 'C':
                color = button_colors['clear']
            elif button_text == '=':
                color = button_colors['equals']
            else:
                color = "#ffffff"  # Blanco por defecto

            self.create_button(button_text, row_val, col_val, color)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, column, color):
        """Crea un botón y lo coloca en la cuadrícula."""
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=("Arial", 18), bg=color, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, char):
        """Maneja los clics en los botones."""
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            self.calculate_result()
        elif char == '√':
            try:
                current_text = self.result_var.get()
                result = math.sqrt(float(current_text))
                self.result_var.set(round(result, 2))
            except ValueError:
                self.result_var.set("Error")
                messagebox.showerror("Error", "Entrada inválida para raíz cuadrada")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def calculate_result(self):
        """Evalúa la expresión ingresada."""
        try:
            expression = self.result_var.get()
            result = self.calculator.evaluate(expression)  # Llama al método evaluate de la clase Calculator
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")
            messagebox.showerror("Error", str(e))

    def run(self):
        """Inicia el bucle principal de la interfaz gráfica."""
        self.master.mainloop()