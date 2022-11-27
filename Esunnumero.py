def esnumero ( a ):
    if a.isnumeric():
        a=int(a)
        return a
    else:
        print('el valor no es un número')
        exit(0)