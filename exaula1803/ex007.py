tupla = (3, 56, 6, 2, 4, 86, 23, 34, 18, 11, 26)

valor = int(input("Digite um número para saber se ele está na tupla: "))

if valor in tupla:
    print(f'O valor {valor} está na tupla!')
else:
    print(f'O valor {valor} não está está na tupla!')