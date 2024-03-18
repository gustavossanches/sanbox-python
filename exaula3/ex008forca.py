palavra = str(input('Digite a palavra para ser adivinhada: '))
chance = 0
palavraEscondida = palavra.__reduce__('', '-')
print(palavraEscondida)

while chance < 5:
    
    chance += 1