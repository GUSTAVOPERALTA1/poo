repeticiones= 0 #Variable que almacena el numero de repeticiones

class Temperaturas:  #Clase principal
	promedio_cent= 0  #Alamacenamos el promedio de °C
	prmedio_fahr= 0  #aAlmacenamos el promedio de °F
	fecha= []  #Almacenamos las fechas
	cent= []  #Almacenamos los °C
	fahr= []  #Almacena los °F

	def __init__(self): #Metodo constructor
		pass

	def datos(self): #Metodo para pedir datos
		dia= input("Deme una fecha: ")  #Pedimos la fecha
		self.fecha.append(dia)#Almacenamos en la variable fecha
		temperatura= int(input("Deme la temperatura en °C: "))#Pedimos la temperatura
		self.cent.append(temperatura) #Almacenamos en cent
		convertir= (temperatura * 9 / 5) + 32 #Convertimos a °F
		self.fahr.append(convertir)#Almacenamos los datos en Fahr

	def mayor(self):#Metodo para encontrar al mayor
		info= dict(zip(self.fahr,self.fecha))#Convertimos los datos a diccionario
		mas= max(info.items(), key=lambda x: x[1]
		)  #Buscamos el mayor elemento, items regresa los datos conjuntos, clave y valor.
		#Key regresa una lista de elementos que seran las claves.
		#lambada convierte la funciona a anonima.
		abrir = open("temperaturas.txt","a")#Abre el archivo para añadir
		abrir.write("Su informacion es la siguiente:  " + str(info) + "\n")#Escribe los datos de diccionario
		abrir.write("La temperatura mayor es: " + str(mas) + "\n") #Escribe la temperatura mayor
		abrir.close()#Cierra el archivo
		print("Temperatura mayor " +str(mas))#Imprime la temperatura y la fecha

	def promedio(self): #Metodo para el promedio
		self.promedio_cent= sum(self.cent)/repeticiones#sacaremos el promedio, primero sumando todos los datos numericos de una tupla
		self.promedio_fahr= sum(self.fahr) /repeticiones #Calculamos el promedio en °f
		print("Promedio fahrenheit:  " + str(
		    self.promedio_fahr) + "\n") #Imprimimos
		print("Promedio centigrados:  " + str(
		    self.promedio_cent) + "\n")  #imprime el pormedio de °f

	def escribir(self):#Metodo para trasladar la informacion
		abrir = open("temperaturas.txt", "a") #Abrimos el archivo
		abrir.write("Promedio centigrados:" + str(self.promedio_cent) + "\n")  #agrega el promedio de °c
		abrir.write("Promedio fahrenheit: " + str(
		    self.promedio_fahr) + "\n")  #agrega el promedio de °f
		abrir.close()  #cierra el archivo


objeto = Temperaturas()  #Declaramos el objeto
repetir = "s"#Variable para repetir
while repetir == "S" or repetir == "s":#Mientras repetir sea s, se ejecutaran los metodos
	repeticiones+= 1  #Sumamos uno a las repeticiones
	objeto.datos() #Llamamos al metodo para pedir datos
	respuesta = input("¿Desea agregar otro dato? s/n ") #Preguntamos si se desea agregar mas datos  
	if respuesta == "N" or respuesta == "n":#Si la respuesta es n, se cierra la primera parte y continuamos
		objeto = Temperaturas()#Se declara un objeto
		objeto.promedio()#Llamamos al metodo para el promedio
		objeto.mayor()#Llamamos al metodo para buscar el mayor
		objeto.escribir()#Llamamos al metodo para escribir en el archivo
		break  #termina el programa
