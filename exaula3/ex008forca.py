palavraEscondida = str(input('Digite a palavra para ser adivinhada: '))
palavraIncompleta = len(palavraEscondida) * '-'

print(palavraIncompleta)
chance = 0
while chance < 5:
    letra = str(input('Digite uma letra da palavra: '))
    for i in palavraEscondida:
        print(i)
    else:
        chance += 1
        print(chance)
