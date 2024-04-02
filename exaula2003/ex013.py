#13. Ordenar os Elementos de uma Lista:

lista = [3, 2, 6, 1, 7, 4, 8, 9, 10]

opc = int(input("Digite '1' para ordem crescente e '2' para decrescente: ")) 

if opc == 1:
    print(f'Lista ordenada em ordem crescente: {sorted(lista)}')
else:
    print(f'Lista ordenada em ordem crescente: {sorted(lista, reverse=True)}')
    