def pedir_datos():
    num = int(input ("digite el numero: "))
    return num

def verificar_num(num):
    if num < 0:
        resultado = ("negativo")
    elif num == 0:
        resultado = ("neutro")
    else:
        resultado = ("positivo")
    return resultado
    
def mostrar_resultado (resultado):
    print (" su numero es:", resultado)

#**************codigo principal**********

num = pedir_datos()
resultado = verificar_num(num)
mensaje = mostrar_resultado(resultado)
