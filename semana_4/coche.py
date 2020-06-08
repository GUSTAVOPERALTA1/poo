class Coche:

    #atributos#
    marca="Ford"
    volante=1
    acientos=5
    ruedas=4
    retrovisores=2

    def __init__(self):
        print("Constructor coche")
    def acelerar(self):
        print("El auto acelera cuando pisas el acelerador")
    def frenar(self):
        print("El auto frena cuando pisas el freno")

class Camioneta(Coche):
    #atributos#
    puertas=4
    viseras=2

    #metodo#
    def __init__(self):
      print("Constructor Camioneta")
    def acelerar(self):
        print("La camioneta acelera cuando cambias la velocidad")
    def frenar(self):
        print("La camioneta frena con el freno de mano")

objeto_coche=Coche()
objeto_coche.acelerar()
objeto_coche.frenar()

objeto_camioneta=Camioneta()
objeto_camioneta.acelerar()
objeto_camioneta.frenar()

camioneta=Camioneta()
print(camioneta.marca)
print(camioneta.volante)
print(camioneta.acientos)
print(camioneta.ruedas)
print(camioneta.retrovisores)
print(camioneta.puertas)
print(camioneta.viseras)