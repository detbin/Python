class alumno:
    nombre = ' '
    nota = 0
    aprobado=True
    def Nombre(self):
        nombre = input('Introduzca el nombre del alumno:')
        return nombre
    def Nota(self):
        nota=input('Introduzca la nota del 1 al 20:')
        if nota.isnumeric():
            return int(nota)
        else:
            print('nota introducida no es valida')
            exit()



alumno= alumno()
Nombre=alumno.Nombre()
Nota=alumno.Nota()
if Nota in range (10,20):
    print('El alumno '+Nombre+' ha sido aprobado')
else:
    if Nota in range (0,10):
        print('El alumno '+Nombre+' ha sido reprobado')
    else:
        print('nota introducida no es valida')
