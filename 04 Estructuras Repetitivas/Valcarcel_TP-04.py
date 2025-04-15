#Ej  1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#cont=0
#entero=0
#for entero in range (0,101,1):
#    print(entero)

#Ej 2) ) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#entero = int(input("Ingrese un número entero: "))
#entero = abs(entero)# abs valor absoluto , evito que cuente un signo como digito
#contador = 0
#if entero==0:
#    contador=1
#else:
#    while entero > 0:
#        entero = entero //10 # utilizo // para que me entregue el valor sin decimal
#        contador += 1
#print ("La cantidad de digitos de la cifra ingresada es: ",contador)

#Ej 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingrese el segundo número: "))
#num1 = abs(num1)
#num2 = abs(num2)
#if num1>num2:
#    num1,num2=num2,num1 #itercambio valores
#suma = 0

#for i in range (num1 +1,num2):
#    suma += i
#print("La suma de los enteros comprendidos entre los números ingresados es :", suma)

#Ej 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
#parar ="0"
#numero = input(f"Ingrese los número que desea sumar. Para finalizar presione  {parar}  ")
#suma = 0

#while numero != parar:
#    suma += int(numero)
##    numero = input(f"Ingrese otro número para sumar. Para finalizar presione  {parar}  ")

##print("La suma de los enteros comprendidos entre los números ingresados es :", suma)

#Ej5 Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número

#from random import *
#numero_aleatorio = randint(0,9)
#intentos = 0
#numero = -1

#while numero != numero_aleatorio:
#    numero = int(input("Ingrese un número, entre 0 y 9 : "))
#    intentos +=1

#print ("usted ha acertado en el intento: ", intentos)

#Ej 6)) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente

#numero_mínimo = 0
#numero_maximo = 100
#while numero_maximo >= numero_mínimo:
#    print (numero_maximo)
#    numero_maximo -=2

#Ej 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario

#numero = int(input("Ingrese un número entero positivo : "))

#suma = 0
#if numero <0:
 #   print ("Debe ingresar un número positivo")
#else:
#    for i in range (0,numero +1):
 #       suma +=i
 #   print ("La suma entre el 0 y el número ingresado es: ", suma)

# Ej 8 ) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).


#cont = 0
#pares= 0
#impares = 0
#positivos =0
#negativos =0
#while cont <100 :
#    cont +=1
#    numero8 = int(input("Ingrese un número: "))
#    if numero8 % 2== 0: 
#        pares +=1
#    
#    else:
#        impares +=1
#    if numero8 >= 0:
#        positivos +=1
# #   else:
#        negativos +=1
#print (" Cantidad de numeros positivos: ", positivos)
#print (" Cantidad de numeros negativos: ", negativos)   
#print (" Cantidad de numeros pares: ", pares) 
#print (" Cantidad de numeros impares: ", impares)

#Ej 9 Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).


#cont = 0
#numero = 0
#media= 0
#numeros = [] #me permite crear una lista donde voy a ir guardando los numeros ingresados , con las llaves, indico que esta vacio al declararlo

#from statistics import mean

#while cont <100 :
    
    #numero = int(input("Ingrese los números enteros para calcular la media: "))
    #numeros.append(numero)
    #cont +=1

#media = mean(numeros) #uso la lista donde se guardaron los numeros ingresados
#print("La media de los números ingresados es: ", media)

#Ej 10 Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Ingrese el númer que desea revertir:" ""))
digito = 0
inverso = 0

while numero > 0:
    digito = numero % 10
    inverso = inverso * 10 + digito
    numero = numero // 10
print ("el numero invertido es : ", inverso)


