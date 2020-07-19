repetir="s" #Variable para while
info=[] #Almacenar los datos
class Alumnos: #Clase primaria
  def __init__(self): #Metodo constructor
    pass

  def info(self): #Metodo donde se pediran datos
    nombre=input("Escribe el nombre del alumno: ") #Pedimos el nombre
    año= int(input("Dame el año de nacimineto del alumno: ")) #Pedimos el año de nacimiento
    grupo=input("Grupo: ") #Pedimos el grupo

    edad=2020-año #Operacion para calcular la edad

    info.append("Nombre:"+str(nombre)+" Edad:"+str(edad)+" Grupo:"+str(grupo)) #Almacenamos los datos en info(arreglo)

  def imprimir(self): #Metodo para imprimir los resultados
    for mostrar in info: #Leemos los datos almacenados en info (arreglo)
      print(mostrar) #Imprimimos los datos

while repetir=="S" or repetir=="s": #Repetir mientras el usuario lo quiera
  objeto_Alumnos= Alumnos() #Llamamos a la clase primaria
  objeto_Alumnos.info() #Llamamos al metodo info 

  repetir=input("¿Desea repetir? s/n") #Preguntamos si se desea repetir
  if repetir== "N" or repetir=="n": #Si la respuesta es no
    objeto_Alumnos.imprimir() #Llamamos al metodo imprimir
    
    