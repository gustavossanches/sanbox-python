tupla = (11, 22, 33, 44, 55, 66, 77, 88, 99, 0)
meio = len(tupla) / 2
index = int(meio)

lista1 = tupla[0:index]
lista2 = tupla[index:]

tupla1 = tuple(lista1)
tupla2 = tuple(lista2)

print(f'Tupla 1: {tupla1}')
print(f'Tupla 2: {tupla2}')
