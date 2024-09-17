# import os
while(True):
    ejercicio = int(input("Elija del 1 al 8 el ejercitario que desea probar, o 0 para salir: "))
  
    if(ejercicio == 1):
        print("1- Hacer un programa que imprima del 10 al 0 en orden decreciente.")

        for i in range(10,-1,-1):
            print(i)

    elif(ejercicio == 2):
        print("2- Hacer un programa que imprima los números pares del 0 al 10.")

        pares = []
        for i in range(0,10):
            if(i % 2 == 0):
                pares.append(i)
        print(f"""
        Los numeros pares del 0 al 10 son:
            {pares}
        """)

    elif(ejercicio == 3):
        print("3- Hacer un programa que imprima la suma de los números del 1 al 10")
        lista = []
        for i in range(0,11):
            lista.append(i)
        print(f"""
                La suma total de los numeros del 1 al 10 es:
                {lista}
                ===> {sum(lista)} <===
                """)
        
    elif(ejercicio == 4):
        print("""
4- Hacer un programa que imprima los números
impares entre el 10 y el cero en orden decreciente y
que calcule la suma de esos números impares.
""")
        impares = []
        for i in range(10,-1,-1):
            if not(i % 2 == 0):
                print(i)
                impares.append(i)
        print(f"""Los numeros impares del 0 al 10 son:
        {impares}
Y la suma total de los numeros impares es de:
        ===> {sum(impares)} <===
""")

    elif(ejercicio == 5):
        print(f"""
5- Hacer un programa que imprima todos los números
enteros que hay desde la unidad hasta un número
que introduciremos por teclado.
""")
        mayor = int(input("Introduce un numero entero: "))
        for i in range(1, mayor + 1):
            print(i)

        
    elif(ejercicio == 6):
        print(f"""
6- Introducir por teclado tantas frases como se desee: 
""")
        frases = []
        while(True):
            frase = input(f"""Ingrese la frase que desee, 
y luego pulse enter para contarlas: 
""")
            if(frase != ""):
                frases.append(frase)
            else:
                print(f"""
            La cantidad de frases introducidas es de:
            {len(frases)}
            """)
                exit()
        
    elif(ejercicio == 7):
        print(f"""
7- Hacer un programa que imprima y cuente los
múltiplos de 3 que hay entre el 0 y el 20.
""")
        multiplos = []
        for i in range(0,21,1):
            if(i % 3 == 0):
                multiplos.append(i)
        print(f"""
              Se imprime la lista de multiplos del 3:
              {multiplos}
              en total son: {len(multiplos)} los multiplos de 3
              contenidos desde el 0 al 20!
              """)
        
    elif(ejercicio == 8):
        print(f"""
8- Ingresar 5 numeros por teclado y al final de los
mismos, el programa debe emitir los siguientes
datos: Suma total, Cantidad de numeros impares, y
un mensaje que indique si existen números
superiores a 100
""")
        
        numeros = []
        impares = []
        mayor100 = "No"
        for i in range(5):
            numero = int(input("Ingresa un numero: "))
            numeros.append(numero)
            if(numero % 2 != 0):
                impares.append(numero)
            if (numero > 100):
                    mayor100 = "Si..."
        print(f"""
                La suma total de los numeros ingresados es de: {sum(numeros)}
                La cantidad de numeros impares es de: {len(impares)}
                Se ha ingresado un numero mayor a 100?: {mayor100}  
                """)

    elif(ejercicio == 0):
        exit()

    else:
        print("El valor es incorrecto!!")

  #  os.system("PAUSE")