#14. Remover um Elemento de uma Lista

lista = [2, 5, 3, 8, 1, 9, 0]

print(f'{lista}')
index = int(input("Digite o index para remover da lista: "))
listaNova = list(lista)
del listaNova[index-1]


print(f'{listaNova}')