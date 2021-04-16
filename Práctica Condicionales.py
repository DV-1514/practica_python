# Condicionales

# 1. 
'''Escribir un programa que pregunte al 
usuario su edad y muestre por pantalla si es mayor de edad o no.'''

#edad=int(input("Coloca tu edad: "))
#if edad < 18:
#    print("Eres menor de edad")
#else:
#    print("Eres mayor de edad")

# 2.
'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el 
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

#contra=input("Coloca la contraseña: ").lower()
#v_1 = "contraseña"
#if v_1 == contra:
#    print("Contraseña Correcta")
#else:
#    print("Contraseña Incorrecta")

# 3.
'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.'''

#dividendo = float(input("Coloca el dividendo: "))
#divisor = float(input("Coloca el divisor: "))
#división = dividendo / divisor
#if divisor == 0:
#    print("No se puede dividir en 0")
#else:
#    print("El resultado es " + str(división))

# Ver por reemplazo de error

# 4.
'''Escribir un programa que pida al usuario un número entero y 
muestre por pantalla si es par o impar.'''

#num = int(input("Coloca un numero entero: "))
#if num % 2 == 0:
#    print("Es par")
#else: 
#    print("es impar")

# 5.
'''Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa 
que pregunte al usuario su edad y sus ingresos mensuales y muestre 
por pantalla si el usuario tiene que tributar o no.'''

#edad = int(input("Coloca tu edad: "))
#ing = float(input("Coloca tus ingresos mensuales: "))
#if edad > 16 and ing > 1000.0:
#    print("Debes tributar impuesto")
#else: 
#    print("No debes tributar impuesto")

# 6.
'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los 
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que 
pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'''

#name = input("¿Cómo te llamas? ")
#gender = input("¿Cuál es tu sexo (M o H)? ")
#if gender == "M":
#    if name.lower() < "m":
#        group = "A"
#    else:
#        group = "B"
#else:
#    if name.lower() > "n":
#        group = "A"
#    else:
#        group = "B"
#print("Tu grupo es " + group)

# 7.
''' Escribir un programa que pregunte al usuario su renta anual 
y muestre por pantalla el tipo impositivo que le corresponde.'''

#renta = float(input("Coloca tu renta anual: "))
#if renta < 10000:
#    print("Tipo impositivo: 5%")
#elif renta < 20000:
#    print("Tipo impositivo: 15%")
#elif renta < 35000:
#    print("Tipo impositivo: 20%")
#elif renta < 60000:
#    print("Tipo impositivo: 30%")
#else: 
#    print("Tipo impositivo: 45%")

# 8.
'''En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden 
ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de 2.400€ 
multiplicada por la puntuación del nivel.'''

'''Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.'''


#puntos = float(input("Coloca tu puntuación: "))
#if puntos == 0:
#    print("Nivel: Inaceptable, Dinero Recibido: 0")
#elif puntos == 0.4:
#    print("Nivel: Aceptable, Dinero Recibido: " + str(0.4 * 2400))
#elif puntos == 0.6:
#    print("Nivel: Meritorio, Dinero Recibido: " + str(0.6 * 2400))

# 9.
'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de 
su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede 
eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''

#print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
#tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
#if tipo == "1":
#    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
#    ingrediente = input("Introduce el ingrediente que deseas: ")
#    print("Pizza vegetariana con mozzarella, tomate y ", end="")
#    if ingrediente == "1":
#        print("pimiento")
#    else: 
#        print("tofu")
#else:
#    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
#    ingrediente = input("Introduce el ingrediente que deseas: ")
#    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
#    if ingrediente == "1":
#        print("peperoni")
#    elif ingrediente == "2":
#        print("jamón")
#    else:
#        print("salmón")




