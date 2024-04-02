conjunto1 = {1, 2, 3, 4, 5, 6, 9}
conjunto2 = {6, 7, 8}

inter = conjunto1.difference(conjunto2)
if inter:
    print(f'A diferença do conjunto é: {inter}')
else:
    print('Não tem diferença!')