# 1.
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#print(asignaturas)

# 2.
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista y la 
# muestre por pantalla el mensaje Yo estudio <asignatura>,
# donde <asignatura> es cada una de las asignaturas de la lista.

#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#for asignaturas in asignaturas:
#    print("yo estudio: " + asignaturas)

# 3. 
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte 
# al usuario la nota que ha sacado en cada asignatura, y después las muestre
# por pantalla con el mensaje En <asignatura> has sacado <nota> donde 
# <asignatura> es cada una des las asignaturas de la lista y 
# <nota> cada una de las correspondientes notas introducidas por el usuario.

#subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#scores = []
#for subject in subjects:
#    score = float(input("¿Qué nota has sacado en: " + subject + "? "))
#    scores.append(str(score))
#for i in range(len(subjects)):
#    print("En " + subjects[i] + " has sacado " + scores[i])

# 4.
# Escribir un programa que pregunte al usuario los números ganadores de la
# lotería primitiva, los almacene en una lista y los muestre por pantalla
# ordenados de menor a mayor.

#awarded = []
#for i in range(6):
#    awarded.append(int(input("Introduce un número ganador: ")))
#awarded.sort()
#print("Los números ganadores son " + str(awarded))

# 5. 
# Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

#mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for i in reversed(mi_lista):
#    print(i, end=", ")

# 6.
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte
# al usuario la nota que ha sacado en cada asignatura y elimine de la lista
# las asignaturas aprobadas. Al final el programa
# debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

#asignaturas = ["Matemática", "Física", "Química", "Historia", "Lengua"]
#for asignatura in asignaturas:
#    nota = (int(input("Coloca tu nota en: " + asignatura + "?")))
#    if nota > 6:
#        asignaturas.remove(asignatura)
#    else:
#        print("Reprobaste " + asignatura)
#print(asignaturas)

#subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#passed = []
##for subject in subjects:
#    score = float(input("¿Qué nota has sacado en " + subject + "?"))
#    if score >= 5:
#        passed.append(subject)
#for subject in passed:
#    subjects.remove(subject)
#print("Tienes que repetir " + str(subjects))


# 7. 
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#for i in range(len(alphabet), 1, -1):
#   if i % 3 == 0:
#       alphabet.pop(i-1)
#print(alphabet)

# 8.
# Escribir un programa que pida al usuario una palabra y
# muestre por pantalla si es un palíndromo.

#palabra = input("Coloca una palabra: ")
#rev_palabra = palabra
#palabra = list(palabra)
#rev_palabra = list(rev_palabra)
#rev_palabra.reverse()
#if palabra == rev_palabra:
#    print("es ")
#else: 
#    print("no es")

