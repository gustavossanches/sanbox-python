#12. Dividir uma Lista em Duas:

lista = [11, 22, 33, 44, 55, 66, 77, 88, 99, 0]
meio = len(lista) / 2
index = int(meio)

lista1 = lista[0:index]
lista2 = lista[index:]

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
