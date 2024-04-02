#2. Encontrar a Soma dos Valores em uma Lista:
#3. Encontrar a Média dos Valores em uma Lista:


lista = []
soma = 0
media = 0

#fazendo a validação da tecla que vai parar o programa (while somente para a verificação)
while True:
    parar = input('Digite a letra que ira parar o programa: ')
    
    #verifica se não é um número e se o tamanho da string é 1
    if(not parar.isdigit() and len(parar)==1):
        print(f'parar -> {parar}')
        break
    else:
        print('Digite apenas uma letra')
print(f'A tecla para parar o programa é {parar}')

while True:
    valor = input('Digite um número ou a tecla de parada "{}" para encerrar e ver a soma: '.format(parar))
    
    #se for digitado um número
    if(valor.isdigit()):
        lista.append(valor)
        
    #qundo clica a tecla de parada
    elif(valor == parar):
        break
    
    #se for digitada outra tecla
    else:
        print('Digite apenas um número ou a tecla de parada')

#verifica o tamanho da lista (ao inves de usar len)
tamanhoLista = 0
for i, v in enumerate(lista):
    tamanhoLista = i
#indice começa em 0 entao no final soma 1 para ficar a quantidade certa
tamanhoLista = tamanhoLista + 1

for j in range(0, tamanhoLista):
    soma += int(lista[j])
    
media = soma/tamanhoLista

print(f'A soma dos valores da lista é : {soma}')
print(f'A media dos valores da lista é : {media:.2f}')

