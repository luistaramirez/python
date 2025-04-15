from ui.interface import CalculatorUI
from calculator import Calculator

def main():
    calculator = Calculator()
    app = CalculatorUI(calculator)
    app.run()

if __name__ == "__main__":
    main()