class vehiculo():
    color=''
    ruedas=0
    puertas=0
class coche(vehiculo):
    velocidad=0
    cilindrada=0
C=coche()
C.velocidad=120
C.cilindrada=1300
C.color='blanco'
C.ruedas=4
C.puertas=4
print(C.velocidad)
print(C.cilindrada)
print(C.color)
print(C.ruedas)
print(C.puertas)
