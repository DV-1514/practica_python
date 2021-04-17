divisa = input("Introduce una divisa: ")

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

print(monedas.get(divisa.title(), "La divisa no está."))
