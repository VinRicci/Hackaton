op =0
justificado=0
listaString= []
justificado= input("Ingrese la cantidad maxima de caracteres por linea: ")

print("Ingrese una cadena de texto:")
listaString.append(input())

while(op == 0):
        print("1.Agregar otra linea")
        print("2.Salir")
        menu = input("Ingrese una opcion: ")
        
        if(menu == "1"):
                print("Ingrese una cadena de texto:")
                listaString.append(input())
        elif(menu== "2"):
                for x in listaString:
                        cadena=x
                        cadena= cadena.replace(" ",".")
                        while(int(len(cadena)) < int(justificado)):
                               cadena= cadena.replace(".",". ") 

                        cadena= cadena.replace("."," ")       
                        print(cadena)

                op = 1
        else:
                print("Opcion invalida")

