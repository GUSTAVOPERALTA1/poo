class Vacaciones:
    #atributos#
    playa="Quintana Roo"
    maletas=3
    gasto="20,000"
    acompañantes=6
    clima="Soleado"

    #metodos#
    def __init__(self):
        print("Vacaciones")

    def nadar(self):
        print("Nadar")
    def pescar(self):
        print("Pesca deportiva")

class Cancun(Vacaciones):
    hotel="Delfin"
    alberca=3

    def __init__(self):
        print("Constructor Cancun")

    def nadar(self):
        print("nadar en alberca")
    def pescar(self):
        print("Pesca con caña")
        
objeto_vacaciones=Vacaciones()
objeto_vacaciones.nadar()
objeto_vacaciones.pescar()

objeto_cancun=Cancun()
objeto_cancun.nadar()
objeto_cancun.pescar()

cancun=Cancun()
print(cancun.playa)
print(cancun.maletas)
print(cancun.gasto)
print(cancun.acompañantes)
print(cancun.clima)
print(cancun.hotel)
print(cancun.alberca)
