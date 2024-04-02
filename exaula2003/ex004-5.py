#4 / 5. Encontrar a Posição do Menor Valor em uma Lista

lista = []

    
#indice começa em 0 entao no final soma 1 para ficar a quantidade certa
#fazendo a validação da tecla que vai parar o programa (while somente para a verificação)
while True:
    parar = input('Digite a letra que ira parar o programa: ')
    
    #verifica se não é um número e se o tamanho da string é 1
    if(not parar.isdigit() and len(parar)==1):
        break
    else:
        print('Digite apenas uma letra')
        
while True:
    valor = input('Digite um número ou a tecla de parada "{}" para encerrar e ver a soma: '.format(parar))
    
    
        
    #se for digitado um número
    if(valor.isdigit()):        
        lista.append(valor)
        print(f'lista -> {lista}')
    
    #qundo clica a tecla de parada
    elif(valor == parar):
        break
    
    #se for digitada outra tecla
    else:
        print('Digite apenas um número ou a tecla de parada')
        
maior = lista[0]
for i in range(0, len(lista)):
    if(lista[i] > maior):
        maior = lista[i]

menor = lista[0]
for i in range(0, len(lista)):
    if(lista[i] < menor):
        menor = lista[i]

print(f'Lista final -> {lista}')
print(f'maior numero -> {maior} na posição -> {lista.index(maior) +1}')
print(f'menor numero -> {menor} na posição -> {lista.index(menor) +1}')






