total = int(input("Ingrese total: "))
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero2: "))
resultado1 = []
cont = 0

if numero1 + numero2 == total:
    while numero1 != 0:
        modulo = numero1 % 2
        cociente = numero1 // 2
        resultado1.append(modulo)
        numero1 = cociente

    while numero2 != 0:
        modulo = numero2 % 2
        cociente = numero2 // 2
        resultado1.append(modulo)
        numero2 = cociente

    for x in resultado1:
        if x == 1:
            cont += 1

    print(f'La abuelita le dara {cont} avellanas')

else:
    print('La suma no coincide')
