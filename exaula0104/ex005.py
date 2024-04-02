'''
5. Ordenação de Elementos:
Crie um conjunto com números de 1 a 10.
Ordene os elementos do conjunto em ordem crescente e decrescente e imprima as listas 
ordenadas
'''
conjunto = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

print(conjunto)

listaConjunto = list(conjunto)
lista = []

for i, v in enumerate(listaConjunto):
    atual = listaConjunto[0]
    if atual > listaConjunto[i+1]:
        listaConjunto[i+1] = atual
        lista.append(listaConjunto[i+1])
print(lista)
