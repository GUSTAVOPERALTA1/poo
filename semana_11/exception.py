import math
enteros=[]
class Excepciones():
  def __init__(self):
    pass

  def numeros(self):
    try:
      valores=int(input("Cantidad de numeros a almacenar: "))
      for i in range(valores):
        valor=int(input("Dame un valor entero: "))
        enteros.append(valor)
    except Exception as error:
      print("Existe un error en los valores insertados",error.args)

objeto_digitos=Excepciones()
objeto_digitos.numeros()

