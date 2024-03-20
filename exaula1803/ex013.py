tupla = (3, 2, 6, 1, 7, 4, 8, 9, 10)

opc = int(input("Digite '1' para ordem crescente e '2' para decrescente: ")) 

if opc == 1:
    print(f'Tupla ordenada em ordem crescente: {sorted(tupla)}')
else:
    print(f'Tupla ordenada em ordem crescente: {sorted(tupla, reverse=True)}')
    