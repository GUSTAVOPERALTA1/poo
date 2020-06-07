class Classroom:

    #atributos#
    tareas="Muchas tareas"
    maestros=9
    clases=6
    materias=9
    fechas="Fechas de entrega"

    def __init__(self):
        print("Classroom constructor")
    def estudiar(self):
        print("Estudiar para hacer bien los trabajos")
    def entregar(self):
        print("Entregar las tareas")

class Guitarra(Classroom):
    guitarra="Usas una guitarra"
    canciones="Aprendes canciones"

    def __init__(self):
        print("Clases de Guitarra constructor")
    def estudiar(self):
        print("Estudiar para aprender más rapido")
    def entregar(self):
        print("Hacer practicas para aprovar")

objeto_classroom=Classroom()
objeto_classroom.estudiar()
objeto_classroom.entregar()

objeto_guitarra=Guitarra()
objeto_guitarra.estudiar()
objeto_guitarra.entregar()

guitarra=Guitarra()
print(guitarra.tareas)
print(guitarra.maestros)
print(guitarra.clases)
print(guitarra.materias)
print(guitarra.fechas)
print(guitarra.guitarra)
print(guitarra.canciones)