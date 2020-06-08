
repetir="s"
while repetir=="s" or repetir=="S": #bucle#
    class Cadenas:
        cadena= input("Dame una cadena") #insertar string#

        def __init__(self):
            pass

    objeto= Cadenas()
    print(objeto.cadena) #imprimir cadena#
    print(len(objeto.cadena)) #Imprimir longuitud de la cadena con espacios#
    print(objeto.cadena.replace(" ","")) #Imprimir cadena sin espacios#
    if objeto.cadena.isalpha()==True or objeto.cadena.islower()==True or objeto.cadena.istitle()==True: #Comparacion de datos#
        print("Cadena de Letras")
    if objeto.cadena.isdigit()==True: #Comparacion numerico#
        print("Cadena Numerica")
    if objeto.cadena.isdecimal()==True: #Comparacion decimal#
        print("Cadena de Decimales")
    print(objeto.cadena.split(" "))#Separar caracteres#
    
    repetir=input("¿Desea analizar otra cadena s/n?:") #Preguntar si se desea reiniciar la operacion#
    
