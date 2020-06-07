class Futbolista:
    #atributos#
    numero=9
    posicion="Delantero"
    tennis="Nike"
    equipo="Necaxa"
    color_uniforme="Rojo"


    #metodos#
    def __init__(self):
        print("Futbolista")

    def patear(self):
        print("El futbolista patea con fuerza")
    def anotar(self):
        print("El jugador ha anotado 23 goles")

class Defensa(Futbolista):
    edad=18
    sexo="Femenino"

    def __init__(self):
        print("Constructor defensa")
        
    def patear(self):
        print("El defensa patea para sacar el balon de su area")
    def anotar(self):
        print("El jugador no ha anotado ningun gol")
        
objeto_futbolista=Futbolista()
objeto_futbolista.patear()
objeto_futbolista.anotar()

objeto_defensa=Defensa()
objeto_defensa.patear()
objeto_defensa.anotar()

defensa=Defensa()
print(defensa.numero)
print(defensa.posicion)
print(defensa.tennis)
print(defensa.equipo)
print(defensa.color_uniforme)
print(defensa.edad)
print(defensa.sexo)
