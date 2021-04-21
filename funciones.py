'''1. Escribir una función que muestre por pantalla el saludo ¡Hola amiga!
 cada vez que se la invoque.'''

#def llamada():
#    print("Hola Amigo")
#    return
#llamada()

'''2. Escribir una función a la que se le pase una cadena <nombre> y 
muestre por pantalla el saludo ¡hola <nombre>!.'''

#def llamada():
#    v=input("Coloca un nombre: ")
#    print("Hola " + v)
#    return
#llamada()

#def llamada(nombre):
#    print("Hola "+ nombre)
#    return
#llamada("Dante")

'''3. Escribir una función que reciba un número entero positivo y 
devuelva su factorial.'''

#def factorial(numero):
#    num=1
#    for i in range(numero):
#        num *= i+1
#    return num
#print(factorial(5))
#print(factorial(4))

'''4.Escribir una función que calcule el total de una factura tras
aplicarle el IVA. La función debe recibir la cantidad sin IVA y el 
porcentaje de IVA a aplicar, y devolver el total de la factura. Si se 
invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''

#def factura(monto, IVA=21):
#    return monto + monto*IVA/100
#print(factura(100, 16))
#print(factura(100))

'''5. Escribir una función que reciba una muestra de números en
 una lista y devuelva su media.'''

#def media(*numeros):
#    return sum(numeros) / len(numeros)
#print(media(1, 5, 7, 8, 9, 15, 20))

'''6. Escribir una función que reciba una muestra de números
en una lista y devuelva otra lista con sus cuadrados.'''

#def cuadrados(*numeros):
#    lista=[]
#    for i in numeros:
#        lista.append(i**2)
#    return lista
#print(cuadrados(2, 3, 4, 5))


'''7. Escribir una función que calcule el máximo común 
divisor de dos números y otra que calcule el mínimo común múltiplo.'''

#def mcd(n, m):
#    rest = 0
#    while(m > 0):
#        rest = m
#        m = n % m
#        n = rest
#    return n

#def mcm(n, m):  
#    if n > m:
#        greater = n
#    else:
#        greater = m
#    while (greater % n != 0) or (greater % m != 0):
#        greater += 1
#    return greater

#print(mcd(12, 24))
#print(mcm(12, 24))




