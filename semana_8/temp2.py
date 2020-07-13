class Temperaturas:
  fecha=[]
  cent=[]
  fahr=[]

  def __init__(self):
    pass

  def datos(self):
    fecha.append(input("Fecha: "))
    cent.append(int(input("Temperatura en °C: "))
    if input("¿Desea repetir? s/n")=="n": break

    convertir= (cent* 9 / 5) + 32 

    mayor= fecha[cent.index(max(cent))]

    print("El mayor registro es: %s" % mayor, ",", "con",(max(cent)), "grados")


objeto= Temperaturas()
objeto.datos()