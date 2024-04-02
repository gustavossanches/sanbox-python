
#6 - 7. quantas vezes aparece e se aparece na lista
lista = []

while True:
    parar = input('Digite a letra que ira parar o programa: ')
    
    #verifica se não é um número e se o tamanho da string é 1
    if(not parar.isdigit() and len(parar)==1):
        break
    else:
        print('Digite apenas uma letra')
        
while True:
    valor = input('Digite um número ou a tecla de parada "{}" para encerrar e ver a soma: '.format(parar))
    
    if(valor.isdigit()):        
        lista.append(valor)
        print(f'lista -> {lista}')
    
    elif(valor == parar):
        break

    else:
        print('Digite apenas um número ou a tecla de parada')

verificar = input('Digite o número que deseja saber: ')
if(verificar.isdigit()):
    if(verificar not in lista):
        print(f'O valor {verificar} não está na lista!')
    else:
        print(f'O valor {verificar} aparece {lista.count(verificar)} vez(es) na lista!')
else:
    print('Digite algum número!')
