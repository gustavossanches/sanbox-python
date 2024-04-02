#. Encontrar o Maior Valor em uma Lista:
lista = []

while True:
    numero = str(input('Digite um número para adicionar à lista ou uma letra para parar: '))
    if numero.isdigit():
        lista.append(int(numero))
    elif len(str(numero)) > 1:
        print('Digite somente uma letra!')
    else:
        break
        
if len(lista) == 0:
    print('lista vazia')
else:
    print(lista)