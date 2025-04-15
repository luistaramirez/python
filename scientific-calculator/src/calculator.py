import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return a ** 0.5

    def exponentiate(self, base, exponent):
        return base ** exponent

    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot compute factorial of a negative number.")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def evaluate(self, expression):
        """Evalúa una expresión matemática."""
        try:
            # Reemplazar operadores personalizados por funciones de Python
            while '√' in expression:
                index = expression.index('√')
                # Buscar el número o expresión después de '√'
                rest = expression[index + 1:]
                if rest.startswith('('):  # Si es una expresión entre paréntesis
                    closing_index = rest.find(')')
                    if closing_index == -1:
                        raise ValueError("Paréntesis no balanceados")
                    inner_expression = rest[:closing_index + 1]
                    expression = expression[:index] + f"round(math.sqrt{inner_expression}, 2)" + rest[closing_index + 1:]
                else:  # Si es un número simple
                    number = ''
                    for char in rest:
                        if char.isdigit() or char == '.':
                            number += char
                        else:
                            break
                    expression = expression[:index] + f"round(math.sqrt({number}), 2)" + rest[len(number):]

            expression = expression.replace('^', '**')  # Reemplazar ^ por ** para exponenciación
            # Evalúa la expresión usando eval
            return eval(expression)
        except Exception:
            raise ValueError("Expresión inválida")
