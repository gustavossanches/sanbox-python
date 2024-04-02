'''
1. Verificação de Elemento:
Crie um conjunto com os nomes de seus amigos.
Peça ao usuário para digitar um nome.
Verifique se o nome está no conjunto e informe o usuário se ele é seu amigo ou não.
'''

conjunto = {'ana', 'bruno', 'carlos', 'eduarda', 'fernanda'}

resposta = ''

while len(resposta) == 0:    
    resposta = input(str('Digite o nome do seu amigo: '))

if resposta in conjunto:
    print(f'{resposta} é seu amigo(a)!')
else:
    print(f'{resposta} não é seu amigo(a)!')    
