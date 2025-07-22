from pila import Pila, PilaVaciaError

class CalculadoraRPN:
    def __init__(self):
        self.pila = Pila()

    def evaluar(self, expresion):
        self.pila.limpiar()
        tokens = expresion.split()
        for token in tokens:
            if token.isdigit():
                self.pila.apilar(int(token))
            elif token in "+-*/":
                try:
                    b = self.pila.desapilar()
                    a = self.pila.desapilar()
                except PilaVaciaError:
                    raise ValueError("Expresión inválida: faltan operandos.")
                if token == '+':
                    self.pila.apilar(a + b)
                elif token == '-':
                    self.pila.apilar(a - b)
                elif token == '*':
                    self.pila.apilar(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("División por cero.")
                    self.pila.apilar(a / b)
            else:
                raise ValueError(f"Token desconocido: {token}")
        if self.pila.esta_vacia():
            raise ValueError("Expresión inválida: sin resultado.")
        resultado = self.pila.desapilar()
        if not self.pila.esta_vacia():
            raise ValueError("Expresión inválida: sobran operandos.")
        return resultado