numero = int(input('Digite um número para ter seu fatorial: '))
fatorial = 1
for numero in range(1, numero+1):
    aux = fatorial
    fatorial = aux*numero
    
print(f'O fatorial de {numero} é {fatorial}')
    