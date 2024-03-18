numero = int(input('Digite um número para ter seu fatorial: '))
i = 1
fatorial = 1

while i < numero+1:
    aux = fatorial
    fatorial = aux*i
    print(fatorial)
    
    i = i + 1