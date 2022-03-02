# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Variables
a = 3
print(type(a))
a = "Hola mundno"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

print("I can't do it")
print('His name is "Sergio"')

#Operaciones
#Suma
a = 5
b = 2 
c = a + b
print(c)

#Resta
a = 5
b = 2 
c = a - b
print(c)

#Multipicacion
a = 5
b = 2 
c = a * b
print(c)

#Divison
a = 5
b = 2 
c = a / b
print(c)

#Division parte entera
a = 5
b = 2 
c = a//b
print(c)

#Potencia
a = 2
c = a ** 6
print(c)

#Raiz cuadrada
a = 16
b  = a ** (1/2)
print(b)

#Raiz cuadrada con immport math
import math 
a = 16
raiz = math.sqrt(a)
print(raiz)

#Raiz cubica
a = 16
b  = a ** (1/3)
print(b)

#Tipos de datos
#String str
a = "Hola mundo"
a = 'Hola mundo'
b = "I can't do it"
c = 'Alias "Checho"'

#Enteron int
a = 5

#Decimal float
a = 5.6

#Booleano Bool

x = True
y = False



#Conversiones entre tipos de datos

#Convertir de x a entero
a = '3'
b = int(a)
print(type(b))

#Convertir de x a decimal
a = '3'
b = float(a)
print(type(b))

#Convertit de x a String
a = 3
b = str(a)
print(type(b))



#Concatenaciones
a = 'hola'
b = 'mundo'
c = a + ' ' + b
print(c)

a = 'hola'
b = a * 5
print(b)

#Capturar por panatalla
nombre = input('Digite su nombre: ')
print('Hola', nombre)


#Interpolacion
nombre = input('Digite su nombre: ')
print(f'Su nombre es: {nombre}')


#Sume dos numeros e imprima su resultado
num1 = int(input('Ingrese el valor del pirmer numero: '))
num2 = int(input('Ingrese el valor del segundo numero: '))
total = num1 + num2
print(f'El resultado de sumar {num1} + {num2} es igual a: {total}')


#Un alg que lea un numero y lo eleve al cuadrado
num = int(input('Ingrese el numero con el que deseas trabajar: '))
total = num ** 2
print(f'El resultado de {num} elevado al cuadrado ({num}^2) es igual a: {total}')


#Un alg que tome el valor de un producto, le aplique el 20%, de descuento,
#imprima el valor del producto inicial, el valor del descuanto y el valor ahorrado
valorIn = int(input('Ingrese el valor del producto que se le aplicará 20% de descuento: '))
valorAho = valorIn * 0.2
valorDesc = valorIn * 0.8
print(f'El valor inicial era de {valorIn}, el valor final es de {valorDesc} y el valor ahorrado es de {valorAho}. ')
