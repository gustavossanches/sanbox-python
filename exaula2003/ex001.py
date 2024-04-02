# achar maior valor da lista

lista = []

while True:
    teclaParar = input('Digite a letra que será usada para parar o programa: ')
    if not teclaParar.isdigit() and len(teclaParar) == 1:
        print(f'A letra tecla para parar o programa é "{teclaParar}"')
        break
    else:
        print('Digite uma letra!')
        
print(teclaParar)

while True:
    valor = input('Digite um número para adicionar na lista ou "{}" para encerrar: '.format(teclaParar))
    if(valor == teclaParar):
        break
    try:
        num = int(valor)
    except ValueError:
        print('Digite um número inteiro!')
    else:
        lista.append(num)

#alternativa para a função len
tamanholista = 0
for i, v in enumerate(lista):
    tamanholista = i
tamanholista = tamanholista + 1 

if(tamanholista > 1):
    maior = lista[0]
    for i in range(1, tamanholista):
        if(lista[i] > maior):
            maior = lista[i]
    if(lista.count(lista[0]) == tamanholista):
        print(f'Todos os valores da lista são iguais: {lista[0]}')
    else:
        print(f'O maior número da lista é {maior}')
elif(tamanholista == 1):
    print(f'A lista possui somente um valor: {lista[0]}')
else:
    print('A lista está vazia!')