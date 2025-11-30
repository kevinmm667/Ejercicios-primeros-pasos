def pedir_dato():
    numero = int (input("digite un numero del 1 al 12: "))
    return numero

def procesar_numero(numero):
    match numero:
     case 1:
          mes= ("enero")
          return mes
     case 2:
          mes= ("febrero")
          return mes
     case 3:
          mes= ("marzo")
          return mes
     case 4:
          mes= ("abril")
          return mes
     case 5:
          mes= ("mayo")
          return mes
     case 6:
          mes= ("junio")
          return mes
     case 7:
          mes= ("julio")
          return mes
     case 8:
          mes= ("agosto")
          return mes
     case 9:
          mes= ("septiembre")
          return mes
     case 10:
          mes= ("octubre")
          return mes
     case 11:
          mes= ("noviembre")
          return mes
     case 12:
          mes= ("diciembre")
          return mes
    
def mostrar_resultado (mes):
     print ("el mes señalado es: ", mes)

#**************codigo principal*****************
numero = pedir_dato()
mes = procesar_numero(numero)
mostrar_resultado (mes)