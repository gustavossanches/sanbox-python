from random import randint

num_sorteado = randint(1, 100)
numero = 0

while numero != num_sorteado:
    numero = int(input("Digite um número até acertar: "))
    if(numero > num_sorteado):
        print('Menor')
    else:
        print('Maior')
print(f'Você acertou! O número correto é {num_sorteado}.')

