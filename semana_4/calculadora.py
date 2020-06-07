class Calculadora:

    #atributos#
    botones=20
    operaciones=13
    pantalla=1
    marca="casio"
    color="Gris"

    def __init__(self):
        print("Constructor calculadora")
    def calcular(self):
        print("Hacer operaciones")
    def jugar(self):
        print("Hacer frases graciosas")

class Barrilito(Calculadora):
    #atributos#
    tapa=1
    iluminacion="tiene leds"

    #metodo#
    def __init__(self):
        print("Barrilito")
    def calcular(self):
        print("Hacer operaciones aritmeticas")
    def jugar(self):
        print("Hacer chistes con una calculadora")

objeto_calculadora=Calculadora()
objeto_calculadora.calcular()
objeto_calculadora.jugar()

objeto_barrilito=Barrilito()
objeto_barrilito.jugar()
objeto_barrilito.calcular()

barrilito=Barrilito()
print(barrilito.botones)
print(barrilito.operaciones)
print(barrilito.pantalla)
print(barrilito.marca)
print(barrilito.color)
print(barrilito.tapa)
print(barrilito.iluminacion)