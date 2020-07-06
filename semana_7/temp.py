class Temperaturas: #Clase primaria
  def __init__(self): #Metodo constructor
    pass
    
  def grados(self): #Metodo
    cent=[] #Variable para almacenar los centigrados
    fahr=[] #Variable para almacenar los fahrenheit
    repetir="s" #Variable para while
    rep=0 #Variable para el numero e repeticiones
    
    while repetir=="S" or repetir=="s": #Condicion para poder repetir el codigo
      rep+=1 #Contor para las repeticioness
      tem= int(input("Dame la temperatura en centigrados: ")) #Pedimos laa temperatura en centigrados
      cent.append(tem) #Almacenamos los datos en la variable cent
      convertir= ((tem*9)/5)+32 #Convertimos los centigrados a fahrenheit
      fahr.append(convertir) #Almacenamos los datos en la variable fhr
      repetir=input("¿Desea repetir? s/n") #Preguntamos si se descea repetir
      
      if repetir=="N" or repetir=="n": #Si se tienen los datos necesarios se frena while
        abrir=open("temperaturas.txt", "a") #Abrimos el archivo de txto
        abrir.write("La temperatura en centigrados es: "+str(cent)+"\n") #Pedimos los datos almacenados en la variable cent
        abrir.write("La temperatura en fahrenheit e: "+str(fahr)+"\n") #Pedimos los datos almacenados en la variable fahr

        promedio_c=sum(cent)/rep #Variable para calcular el promedio de cent
        promedio_f=sum(fahr)/rep #Variable para calcular el promedio de fahr

        abrir.write("Promedio de grados centigrados: "+str(promedio_c)+"\n") #Escribimos el promedio en el archivo de texto
        abrir.write("Promedio de grados fahrenheit:"+str(promedio_f)+"\n")  #Escribimos el promedio en el archivo de texto ahora en fahrenheit
        abrir.close() #Cerramos el archivo
        print("El promedio de grados centigrados es: "+str(promedio_c)) #Imprimimos los resultados 
        print("El promedio de grados fahrenheit es: "+str(promedio_f)) #Imprimimos el resultado en la pantalla
        break #Termina el programa
        
objeto_medida=Temperaturas() #Llamamos a la clase
objeto_medida.grados()#Llamamos al metodo