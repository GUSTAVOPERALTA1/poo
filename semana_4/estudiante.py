class Estudiante:
    #atributos#
    materias=9
    color_uniforme="Azul"
    escuela="UTEC"
    maestros=8
    aula=23

    #metodos#
    def __init__(self):
        print("Estudiante")

    def estudiar(self):
        print("Estudiar medicina")

    def aprender(self):
        print("Aprender de sus maestros")


class Gustavo(Estudiante):
    edad=18
    promedio=8

    def estudiar(self):
        print("Estudio para mis examenes")
    def aprender(self):
        print("Aprender programacion")

objeto_estudiante=Estudiante()
objeto_estudiante.estudiar()
objeto_estudiante.aprender()

objeto_gustavo=Gustavo()
objeto_gustavo.estudiar()
objeto_gustavo.aprender()

gustavo=Gustavo()
print(gustavo.materias)
print(gustavo.color_uniforme)
print(gustavo.escuela)
print(gustavo.maestros)
print(gustavo.aula)
print(gustavo.edad)
print(gustavo.promedio)
