palavraEscondida = str(input('Digite a palavra para ser adivinhada: '))
palavraIncompleta = len(palavraEscondida) * '-'

print(palavraIncompleta)
print('teste -> ',palavraIncompleta[2])
chance = 0
while chance < 5:
    letra = str(input('Digite uma letra da palavra: '))
    for index, i in enumerate(palavraEscondida):
        if letra == i:
            print(letra)
            palavraIncompleta[index] = letra
        print(palavraIncompleta)
    
    else:
        chance += 1
        print(chance)
    
