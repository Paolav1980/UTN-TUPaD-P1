#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int (input("Ingrese su edad: "))
if edad > 18:
    print (f"Usted tiene {edad}  años. Es mayor de edad ")
else:
    print ("Usted es menor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int (input("Ingrese su nota"))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int (input("Ingrese un número par :"))
if num % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años

edad = int (input ("Ingrese su edad : "))
if edad <12:
    print (" Usted pertenece a la categoría NIÑO ")
elif edad >= 12 and edad <=18:
    print(" Usted pertenece a la categoría ADOLESCENTE")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoría ADULTO/JOVEN ")
else:
    print("Usted pertenece a la categoría ADULTO/MAYOR")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python p

contraseña = input("Ingrese su contraseña, debe contener entre 8 y 14 caracteres: ")

if 8<=len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña que tenga entre 8 y 14 caracteres")


#6)
import random

from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1,100)for i in range (50)]
moda = mode(numeros_aleatorios)
print (f"la Moda de los números aleatorios es:{moda}")
mediana = median(numeros_aleatorios)
print (f"la Mediana de los números aleatorios es:{mediana}")
media = mean(numeros_aleatorios)
print (f"la Media de los números aleatorios es:{media}")
if media > mediana and mediana > moda:
    print ("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print ("Hay sesgo negativo o a la izquierda")   
elif media == mediana and mediana == moda:
    print ("No hay sesgo")


#7)
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.

frase = input ("ingrese una palabra o frase:  ")
vocales = "aeiouAEIOU" #defino las vocales
#verificar si el ultimo caracter es una vocal
if frase and frase[-1] in vocales:
    print (f"Usted ingresó:   {frase}!")
else:
    print (f"Usted ingresó:   {frase}")


#8)
nombre = str(input ("Ingrese su nombre: "))
print (f"Hola {nombre} selecciona una de las siguientes opciones")
print ("1 Si quiere su nombre en mayúsculas")
print ("2  Si quiere su nombre en minúsculas.")
print ("3 Si quiere su nombre con la primera letra mayúscula.")

numero = int (input("Ingrese el la opción que desee: "))
if numero == 1:
    print (nombre.upper())# Upper debe estar contiguo de (), pasa el texto a mayúscula
elif numero == 2:
    print (nombre.lower())#lower debe estar contiguo de (), pasa el texto a minúscula
elif numero ==3:
    print (nombre.title())# tittle debe estar contiguo de (), hace que la primer letra esté en mayúscula
else: 
    print ("Por favor, ingrese una opción válida")


#9)
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = int(input("Ingrese la magnitud del terremoto : "))
if magnitud <3:
    print ("Según la escala de Ritcher el terremoto ha sido de magnitud IMPERCEPTIBLE")
elif magnitud >= 3 and magnitud <4:
    print ("Según la escala de Ritcher el terremoto ha sido de magnitud LEVE,ligeramente imperceptible ")
elif magnitud >=4 and magnitud <5:
    print ("Según la escala de Ritcher el terremoto ha sido de magnitud MODERADO, sentido por personas, generalmente no cauda daños   ")
elif magnitud >=5 and magnitud <6:
    print ("Según la escala de Ritcher el terremoto ha sido de magnitud FUERTE, puede causar daños en estructuras DÉBILES")
elif magnitud >=6 and magnitud <7:
    print ("Según la escala de Ritcher el terremoto ha sido de magnitud MUY FUERTE, puede causar daños significativos ")
elif magnitud >=7:
    print ("Según la escala de Ritcher el terremoto ha sido de magnitud EXTREMO, puede causar graves daños a gran escala  ")
else:
    print ("verifique el caracter ingresado.")


#10)
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio = input("Ingrese el hemisferio en el cual se encuentra N/S: ").strip().upper() #upper() convierte todos los caracteres de una cadena a mayúsculas, 
#strip() elimina los espacios en blanco al principio y al final de una cadena
mes = int(input ("Ingrese en números el mes del año en el que se encuentra: "))
dia = int(input("Ingrese en cifras, el día en el que se encuentra: "))
if hemisferio == "N":
    if (mes ==12 and dia >21) or (1<=mes>=2) or (mes ==3 and dia <=20):
     print ("Usted está en Invierno")
    elif (mes ==3 and dia >21) or (4<=mes>=5 )or (mes ==6 and dia <=20):
     print ("Usted está en Primavera") 
    elif (mes ==6 and dia >21) or (7<=mes>=8 ) or (mes ==9 and dia <=20):
     print ("Usted está en Verano")
    else:
       print ("Usted está en Otoño")
if hemisferio == "S":
    if (mes ==12 and dia >=21) or (1<=mes>=2 ) or (mes ==3 and dia <=20):
     print ("Usted está en Verano")
    elif (mes ==3 and dia >21) or (4<=mes>=5 ) or (mes ==6 and dia <=20):
     print ("Usted está en Otoño") 
    elif (mes ==6 and dia >21) or (7<=mes>=8 )or (mes ==9 and dia <=20):
     print ("Usted está en Invierno")
    else:
       print ("Usted está en Primavera")
else:
  print ("Recuerde que debe ingresar N/S para el hemisferio")
