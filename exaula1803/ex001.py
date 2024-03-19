
#simples sem validação e tratamento de 'resp'
x = 0
resp = 's'
while resp == 's':
    lista = []
    x = int(input("Digite um número para adicionar à lista: "))
    lista.append(x)
    resp = str(input("Quer continuar[s / n]: "))
    
tupla = tuple(lista)


print(f'Maior número da tupla é: {max(tupla)}')