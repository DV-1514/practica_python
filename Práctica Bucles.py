# 1.
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
#p = input("Escribe una palabra: ")
#for i in range(10):
#    print(p)

# 2.
# Escribir un programa que pregunte al usuario su edad y 
# muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
#edad = int(input("Coloca tu edad: "))
#for i in range(1, edad+1):
#    print(i)

# 3.
# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número separados por comas.
#num=int(input("Coloca un numero entero positivo: "))
#for i in range(1, num+1, 2):
#    print(i, end=",")

# 4.
#Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla la cuenta atrás desde ese número hasta cero separados por comas.
#n = int(input("Coloca un numero entero positivo: "))
#for i in range(n, -1, -1):
#    print(i, end=",")

# 5. 
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
# anual y el número de años, y muestre por pantalla el capital obtenido en la 
# inversión cada año que dura la inversión.
#amount = float(input("¿Cantidad a invertir? "))
#interest = float(input("¿Interés porcentual anual? "))
#years = int(input("¿Años?"))
#for i in range(years):
#    amount *= 1 + interest / 100 
#    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

# 6.
#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#n = int(input("Introduce la altura del triángulo (entero positivo): "))
#for i in range(n):
#   print("*"*(i+1))

# 7.
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
#for i in range(1, 11):
#    for j in range(1, 11):
#        print(i*j, end="\t")
#    print("")

# 8.
# Escribir un programa que pida al usuario un número entero y muestre por pantalla 
# un triángulo rectángulo como el de más abajo.

#n = int(input("Introduce la altura del triángulo (entero positivo): "))
#for i in range(1, n+1, 2):
#    for j in range(i, 0, -2):
#        print(j, end=" ")
#    print("")

# 9.
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

#cont=input("Coloca la contraseña: ")
#contra = "contraseña"
#while cont != contra:
#    print("Contraseña Incorrecta")
#    cont=input("Coloca la contraseña: ")
#print("Contraseña Correcta")

# 10.
#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es un número primo o no.

#n = int(input("Introduce un número entero positivo mayor que 2: "))
#i = 2
#while n % i != 0:
#    i += 1
#if i == n:
#    print(str(n) + " es primo")
#else:
#    print(str(n) + " no es primo")

#n = int(input("Introduce un número entero positivo mayor que 2: "))
#for i in range(2, n):
#    if n % i == 0:
#        break
#if (i + 1)  == n:
#    print(str(n) + " es primo")
#else: 
#    print(str(n) + " no es primo")


# 11.
#Escribir un programa que pida al usuario una palabra y luego muestre por 
#pantalla una a una las letras de la palabra introducida empezando por la última.

#palabra = input("Coloca una palabra: ")
#for i in range(len(palabra)-1, -1, -1):
#    print(palabra[i])


# 12.
#Escribir un programa en el que se pregunte al usuario por una frase y una letra,
#y muestre por pantalla el número de veces que aparece la letra en la frase.

#palabra=input("Coloca una frase: ")
#letra=input("Coloca una letra: ")
#contador = 0
#for i in palabra:
#    if i == letra:
#        contador += 1
#print("La letra " + letra + " aparece " + str(contador) + " veces.")

# 13.
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
# hasta que el usuario escriba “salir” que terminará.

#palabra=input("Escribe algo: ").lower()
#clave = "salir"
#while palabra != clave:
#    palabra=input("Escribe algo: ")
#if palabra == clave:
#    print("Sesión Terminada")


#mas sensillo

#while True:
#    frase = input("Introduce algo: ")
#    if frase == "salir":
#        break
#    print(frase)

