class Serie:
    #atributos#
    personajes=30
    canal="Warner"
    genero="Accion"
    temporadas="3 Temporadas"
    capitulos="60 capitulos"


    #metodos#
    def __init__(self):
        print("Serie de TV")

    def entretener(self):
        print("La serie entretiene por su trama")
    def intrigar(self):
        print("La trama te intriga")

class Daredevil(Serie):
    protagonista="Daredevil"
    estado="Cancelada"

    def __init__(self):
        print("Constructor Daredevil")

    def entretener(self):
        print("Esta temporada es entretenida")
    def intrigar(self):
        print("Te intrigan sus episodios")
        
objeto_serie=Serie()
objeto_serie.entretener()
objeto_serie.intrigar()

objeto_daredevil=Daredevil()
objeto_daredevil.entretener()
objeto_daredevil.intrigar()

daredevil=Daredevil()
print(daredevil.personajes)
print(daredevil.canal)
print(daredevil.genero)
print(daredevil.temporadas)
print(daredevil.capitulos)
print(daredevil.protagonista)
print(daredevil.estado)