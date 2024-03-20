resp = "s"
tupla = tuple()
while resp == "s":
    lista = list(tupla)
    x = int(input("Digite um número para adicionar à lista: "))
    lista.append(x)
    resp = str(input("Quer continuar[s / n]: "))
    tupla = tuple(lista)

soma = sum(lista)
print(f"Tupla inicial: {tupla}")
print(f"Soma dos valores da tupla: {soma}")
