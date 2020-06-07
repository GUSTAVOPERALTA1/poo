class Cajero:
    #atributos#
    botones=15
    color="Gris"
    pantalla=1
    camara=1
    bandejas=2

    def __init__(self):
        print("Cajeros automaticos")
    def retirar(self):
        print("Puedes hacer retiros de efectivo")
    def consultar(self):
        print("Puedes consultar tu saldo")

class Bancomer(Cajero):
    velocidad="Rapidos"
    material="Metal"

    def __init__(self):
        print("Cajeros bancomer")
    def retirar(self):
        print("Puedes retirar tu dinero")
    def consultar(self):
        print("Consulte su saldo aqui")

objeto_cajero=Cajero()
objeto_cajero.retirar()
objeto_cajero.consultar()

objeto_bancomer=Bancomer()
objeto_bancomer.retirar()
objeto_bancomer.consultar()

bancomer=Bancomer()
print(bancomer.botones)
print(bancomer.color)
print(bancomer.pantalla)
print(bancomer.camara)
print(bancomer.bandejas)
print(bancomer.velocidad)
print(bancomer.material)