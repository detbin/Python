#PROGRAMA PARA DETERMINAR SI UN AÑO ES BISIESTO
def bisiesto(year):
    if year%4 == 0:
        return True
print ('PROGRAMA PARA DETERMINAR SI UN AÑO ES BISIESTO')
Year=int(input('Introduce el año:'))
if bisiesto(Year):
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')
