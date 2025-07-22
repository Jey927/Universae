from calculadora import CalculadoraRPN

def main():
    calc = CalculadoraRPN()
    print("Calculadora RPN (postfija). Ejemplo: 3 4 + 2 *")
    while True:
        expr = input("Introduce expresión RPN (o 'salir'): ")
        if expr.lower() == "salir":
            print("¡Hasta luego!")
            break
        try:
            resultado = calc.evaluar(expr)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()