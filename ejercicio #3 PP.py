def pedir_dato ():
    num = int (input("escriba el numero: "))
    return num

def verificar_numero(num):
    if num%2==0:
        decir = ("el numero es par")
        return decir
    else:
        decir =("el numero es impar")
        return decir
    
def mostrar_mensaje (decir):
    print (decir)

#codigo pricipal

num = pedir_dato()
verificacion = verificar_numero(num)
mostrar_mensaje(verificacion)
