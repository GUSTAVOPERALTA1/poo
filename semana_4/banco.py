class Banco:

    #atributos#
    no_cuentas=24
    oficinas=6
    cajeros_automaticos=5
    ventanillas=5
    sillas=10
    
    def __init__(self):
        print("Banco")

    def pagar(self):
        print("Realiza tus pagos aquí")

    def depositar(self):
        print("Realiza tus depositos aquí")

        
class Banamex(Banco):
    slogan="El mejor banco de Mexico"
    logo="Azul"
    
    def __init__(self):
        print("Constructor Banamex")
    def pagar(self):
        print("Puedes pagar aqui")
    def depositar(self):
        print("Banamex, puedes depositar aqui")


objeto_banco=Banco()
objeto_banco.pagar()
objeto_banco.depositar()


objeto_banamex=Banamex()
objeto_banamex.pagar()
objeto_banamex.depositar()

banamex=Banamex()
print(banamex.no_cuentas)
print(banamex.oficinas)
print(banamex.cajeros_automaticos)
print(banamex.ventanillas)
print(banamex.sillas)
print(banamex.slogan)
print(banamex.logo)

