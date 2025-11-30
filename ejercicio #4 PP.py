def pedir_cantidad ():
    cant = int(input("digite la cantidad de datos: "))
    return cant

def pedir_numero ():
    num = int(input("ingrese el numero: "))
    return num

def procesar_numero (cant):
    suma = 0
    for i in range (cant):
        num = pedir_numero()
        suma += num
    return suma

def mostrar_mensaje (suma):
    print ("el total es: ", str(suma))

#*************codigo principal******************
cantidad = pedir_cantidad()
total = procesar_numero(cantidad)
mostrar_mensaje (total)

