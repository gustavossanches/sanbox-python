'''
1. Verificação de elemento em conjunto:
Escreva um programa que verifique se um determinado elemento está presente em um conjunto. 
Utilize if e else para exibir mensagens informativas.
'''

valores = []
conjunto = set()
novoConjunto = set()

while True:
    parar = input('Digite a letra que ira parar o programa: ')
    
    if(not parar.isdigit() and len(parar)==1):
        break
    else:
        print('Digite apenas uma letra')
        
while True:
    valor = input('Digite um número ou a tecla de parada "{}" para encerrar e ver a soma: '.format(parar))
    
    if(valor.isdigit()):    
        valores.append(valor) 
        conjunto = set(valores)
    
    elif(valor == parar):
        break

    else:
        print('Digite apenas um número ou a tecla de parada')
        
verificar = input('Digite um valor para saber se está no conjunto: ')
for i in conjunto:
    if(i == verificar):
        print(f'O valor {verificar} está no conjunto!')
    else:    
        print(f'O valor {verificar} não está no conjunto!')
print(f'conjunto -> {conjunto}')
