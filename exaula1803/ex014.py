tupla = (2, 5, 3, 8, 1, 9, 0)

print(f'{tupla}')
index = int(input("Digite o index para remover da tupla: "))
listaNova = list(tupla)
del listaNova[index-1]


print(f'{listaNova}')