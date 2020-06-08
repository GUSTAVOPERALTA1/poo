class Avion:
    #atributos#
    alas=2
    alerones=3
    turbinas=5
    piloto=2
    destino="Miami"

    #metodos#
    def __init__(self):
        print("Avion")

    def volar(self):
        print("El avion vuela muy rapido")

    def aterrizar(self):
        print("El avion usa el tren de aterrizaje")

class Concorde(Avion):
    velocidad="2.179 km/h"
    motor="Rolls-Royce/Snecma Olympus 593"

    def __init__(self):
        print("Constructor Concorde")

    def volar(self):
        print("El Concorde rompe la barrera del sonido")
    def aterrizar(self):
        print("El Concorde aterriza silenciosamente")


objeto_avion=Avion()
objeto_avion.volar()
objeto_avion.aterrizar()

objeto_concorde=Concorde()
objeto_concorde.volar()
objeto_concorde.aterrizar()

concorde=Concorde()
print(concorde.alas)
print(concorde.alerones)
print(concorde.turbinas)
print(concorde.piloto)
print(concorde.destino)
print(concorde.velocidad)
print(concorde.motor)
  