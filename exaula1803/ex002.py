
x = 0
resp = 's'
while resp == 's':
    lista = []
    x = int(input("Digite um número para adicionar à lista: "))
    lista.append(x)
    resp = str(input("Quer continuar[s / n]: "))
    
print(f'lista: {lista}')
tupla = tuple(lista)

soma = sum(list(tupla))


print(f'Tupla inicial: {tupla}')
print(f'Soma dos valores: {soma}')