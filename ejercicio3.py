cadena1 = input("Ingrese la primer cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
resultado = ""
esp = ""


if(len(cadena1) > len(cadena2)):
        espacios = len(cadena1) - len(cadena2)
        for i in range(espacios):
            esp += " "
        cadena2 = cadena2 + esp
        for x in range(len(cadena1)):
                if(cadena1[x] == cadena2[x]):
                        resultado=resultado + cadena1[x]
                
else:
        espacios = len(cadena1) - len(cadena2)
        for i in range(espacios):
            esp += " "
        cadena2 = cadena2 + esp
        for x in range(len(cadena2)):
                if(cadena1[x] == cadena2[x]):
                        resultado=resultado + cadena2[x]
                

print("respuesta: "+resultado)