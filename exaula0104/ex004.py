'''
4. Subconjuntos:
Crie um conjunto com os países da América do Sul e outro com os países que você já visitou.
Verifique se o conjunto dos países que você já visitou é um subconjunto do conjunto dos países 
da América do Sul
'''


conjunto1 = {'Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai'}
conjunto2 = {'Brasil', 'Coreia do Norte', 'Paquistão', 'Paraguai', 'Senegal'}
conjunto3 = conjunto2.issubset(conjunto1)

if conjunto3:
    print(f'Os países que você visitou não são um subconjunto dos países da América do Sul!')
else:
    print(f'Os países que você visitou são um subconjunto dos países da América do Sul!')
