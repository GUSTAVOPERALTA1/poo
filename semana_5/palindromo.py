repetir="s"
while repetir=="s" or repetir=="S": #bucle#
    class Palindromo:  #declaración de la clase#
        def __init__(self):  #constructor#
            pass

        def cadena(self): 
            frase= input("Escribe una frase: ")  #Se usa un input para pedir la cadena#
            espacios= 0 #Almacenara el numero de espacios#
            cadena= frase.lower()  #Buscar las minusculas (se transforma todo el codigo a minuscula)#
            for espacio in cadena: #Asigna el rango a revisar para los espacios#
                if espacio in " ": #Si encuentra un espacio lo mandara a almacenar a la variable espacios#
                    espacios+=1 #almacenamiento de los espacios#
            print("Espacios: "+str(espacios)) #Imprime el numero de espacios almacenados en la variable anterior#
            
            frase= frase.lower()#Convierte todas las letras en minisculas#
            frase= frase.replace(" ", "") #Eliminar espacios en la cadena#
            frase= frase.replace("á","a") #Elimina los acentos#
            frase= frase.replace("é", "e")
            frase= frase.replace("í", "i")
            frase= frase.replace("ó", "o")
            frase= frase.replace("ú", "u")
            vocal= 0 #almacena el numero de vocales#
            for vocales in cadena: #Asigna el rango a revisar#
                if vocales in "aeiouáéíóú": #Compara las vocales para saber cuantas son#
                    vocal+= 1 #Almacena las vocales#
            print("Vocales: "+str(vocal))
            inv= ""  # Almacenar la cadena invertida#
            for i in frase:  #Se asigna el rango a revisar, iniciando por la ultima letra#
                inv= i + inv  #El valor de la variable sera la cadena en si, pero de atras para adelante#
            if frase== inv:  # Comparar la cadena con su version invertida para saber si es un Palindromo#
                print("Palindromo")  #Si es igual se imprime el mensaje#
            else: #Si no, se ejecuta esta acción#
                print("No es palindromo")  #Si no se cumple la igualdad se imprime esta frase#


    objeto_igualdad = Palindromo()#Llamado a la clase objeto#
    objeto_igualdad.cadena()#Se llama al metodo cadena
    repetir=input("¿Desea repetir? s/n") #Respuesta del ciclo while para repeticion#