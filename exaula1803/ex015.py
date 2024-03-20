tupla = tuple()
valor = int(input("Digite um valor para adicionar na tupla: "))

lista = list(tupla)
lista.append(valor)
tupla = tuple(lista)

print(tupla)