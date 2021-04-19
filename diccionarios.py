'''1. Escribir un programa que guarde en una variable el diccionario {'Euro':
'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre 
su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

# divisa = input("Introduce una divisa: ")
# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# print(monedas.get(divisa.title(), "La divisa no está."))

'''2. Escribir un programa que pregunte al usuario su nombre, edad, dirección 
y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla 
el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
teléfono es <teléfono>.'''

# dat_nom = input("Coloca tu nombre: ")
# dat_edad= input("Coloca tu edad: ")
# dat_dir=input("Coloca tu dirección: ")
# dat_tel=input("Coloca tu telefóno: ")
# datos={"Nombre":dat_nom, "edad":dat_edad, "Dirección":dat_dir, "Telefono":dat_tel}
# print(datos["Nombre"] + " tiene " + datos["edad"] + " años, vive en " + datos["Dirección"] + " y su telefono es " + datos["Telefono"])

'''3. Escribir un programa que guarde en un diccionario los precios de las frutas
de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre
por pantalla el precio de ese número de kilos de fruta. Si la fruta no está
en el diccionario debe mostrar un mensaje informando de ello.'''

#frutas={"Plátano":1.35, "Manzana":0.8, "Pera":0.85, "Naranja":0.70}
#eleccion=input("Elige una fruta: ").title()
#peso=int(input("dime cuantos kilos: "))
#if eleccion in frutas:
#    print(peso, "kilos de ", eleccion, "valen", frutas[eleccion]*peso)
#else:
#    print("no esta esa fruta")

'''4. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde 
<mes> es el nombre del mes.'''

#meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
#fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
#fecha = fecha.split('/')
#print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])

'''5. Escribir un programa que almacene el diccionario con los créditos de las
asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del
curso, y <créditos> son sus créditos. Al final debe mostrar también el número
total de créditos del curso.'''

#curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
#total_creditos = 0
#for asignatura, creditos in curso.items():
#    print(asignatura, 'tiene', creditos, 'créditos')
#    total_creditos += creditos
#print('Número total de créditos del curso: ', total_creditos)

'''6. Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo 
dato debe imprimirse el contenido del diccionario.'''

#persona = {}
#continuar = True
#while continuar:
#    clave = input('¿Qué dato quieres introducir? ')
#    valor = input(clave + ': ')
#    persona[clave] = valor
#    print(persona)
#    continuar = input('¿Quieres añadir más información (Si/No)? ').title() == "Si"

'''7. Escribir un programa que cree un diccionario simulando una cesta de la
 compra. El programa debe preguntar el artículo y su precio y añadir el par 
 al diccionario, hasta que el usuario decida terminar. Después se debe mostrar
  por pantalla la lista de la compra y el coste total, con el siguiente formato'''

#compras={}
#agregar=True
#total=0
#while agregar:
#    clave=input("Articulo: ")
#    valor=float(input(clave + ": precio: "))
#    compras[clave]=valor
#    agregar=input("agregas mas.?").title() == "Si"
#for clave, valor in compras.items():
#    print(clave, "\t", valor)
#    total+=valor
#print("total" "\t", total)

'''8. Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un
diccionario con las palabras y sus traducciones. Después pedirá una frase en 
español y utilizará el diccionario para traducirla palabra a palabra. Si una 
palabra no está en el diccionario debe dejarla sin traducir.'''

#diccionario = {}
#palabras = input("Introduce la lista de palabras y traducciones en formato <palabra:traducción> separadas por comas: ")
#for i in palabras.split(","):
#    clave, valor = i.split(':')
#    diccionario[clave] = valor
#frase = input('Introduce una frase en español: ')
#for i in frase.split():
#    if i in diccionario:
#        print(diccionario[i], end=' ')
#    else:
#        print(i, end=' ')

'''# Cadena con los datos de los clientes de la empresa
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# Dividimos la cadena por el caracter de cambio de línea \n y creamos una lista con las subcadenas
lista_clientes = datos_clientes.split('\n')
# Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
directorio = {}
# Dividimos la cadena del primer elemento de la lista de clientes (que contienen los 
# nombres de los campos) por el caracter ; y creamos una lista con los campos.
lista_campos = lista_clientes[0].split(';') 
# Bucle iterativo para recorrer los elementos de la lista lista_clientes.
# la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista 
# (el primer elemento contiene los nombres de campo así que no corresponde a un cliente)
for i in lista_clientes[1:]:
    # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
    cliente = {}
    # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
    # información del cliente
    lista_info = i.split(';') 
    # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
    # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde 
    # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
    # principal
    for j in range(1,len(lista_campos)):
        # Condicional. Si el campo actual es descuento convertimos su valor en real
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    # Añadirmos un par al diccionario del directorio con la clave el nif del cliente y valor
    # el diccionario que acabamos de crear con el resto de sus datos.
    directorio[lista_info[0]] = cliente
# Mostramos el diccionario por pantalla
print(directorio)'''





