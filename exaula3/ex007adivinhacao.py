from random import randint

secreto = randint(1, 100)
numero = 0

while numero!= secreto:
    numero = int(input("Digite um número: "))
    if(numero > secreto):
        print('Menos!')
    else:
        print('Mais!')

print(f'Você acertou! O número correto é {secreto}')