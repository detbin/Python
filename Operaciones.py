class Op:
    def suma(*args):
        resultado=0
        for arg in args:
            resultado += arg
        return resultado
    def resta(*args):
        print(args)
        resultado=int(args[0])
        print(resultado)
        for arg in args:
            resultado = resultado-arg
        return (resultado+args[0])
    def multiplica(*args):
        resultado=1
        for arg in args:
            resultado =resultado* arg
        return resultado
    def divide( a, b):
        resultado=(a/b)
        return resultado
