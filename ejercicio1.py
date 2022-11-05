contador = 0

cadena1 = input("Ingrese primera Cadena: ")
cadena2 = input("Ingrese segunda Cadena: ")

cadena1=cadena1.upper()
cadena2=cadena2.upper()

cadena1 =cadena1.replace(" ","")
cadena2 =cadena2.replace(" ","")

tamaño = len(cadena1)
print(cadena1)
print(cadena2)

bandera = 0
if( len(cadena1) == len(cadena2)):
        bandera = 1

def remover(s, n):
    inicio = 0
    fin = len(s)
    resultado = s[inicio:n] + s[n+1:fin]
    return resultado

contadorx = 0
contadory = 0
for x in cadena1:
        for y in cadena2:
                if(y == x):
                        cadena1=remover(cadena1,contadorx)
                        cadena2=remover(cadena2,contadory)                
                        contador = contador + 1
                contadory=contadory+1
        contadorx=contadorx+1
        contadory=0

if(contador == tamaño and bandera == 1):
        print("TRUE")
else:
        print("FALSE")
                

