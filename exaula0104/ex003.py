'''
3. Diferença de Conjuntos:
Crie um conjunto com os livros que você já leu e outro com os livros que você deseja ler.
Encontre os livros que você ainda não leu e imprima a lista
'''

conjunto1 = {'código limpo', 'a cidade do sol', 'jogos vorazes', 'em chamas'}
conjunto2 = {'a revolta', 'o ladrão de raios', 'quarta asa', 'harry potter'}
conjunto3 = conjunto2.difference(conjunto1)

if len(conjunto3) != 0:
    print(f'Os livros que você quer ler são: {conjunto3}!')
else:
    print(f'Vocês não tem livros que deseja ler!')    
