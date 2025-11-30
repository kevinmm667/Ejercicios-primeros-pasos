def dar_opcion():
        print ("digite la letra 'A' para actualizar sistema")
        print ("digite la letra 'E' para eliminar catalogo")
        print ("digite la letra 'C' para crear productos")
        print ("digite la letra 'S' para salir el programa")

def elegir_op():
    letra = (input("digite su opcion: "))
    return letra

def verificar_respuesta (letra):

    if letra  == 'A':
        print ("actualizando sistema...")
    elif letra == 'E':
        print ("eliminando catalogo...")
    elif letra == 'C':
        print ("creando productos...")
    else:
        print ("finalizo!")

#**********codigo principal************
while True:
    dar_opcion()
    letra = elegir_op()
    verificar_respuesta(letra)
    
    if letra =='C':
     break
     
print("proceso finalizado.")
    
