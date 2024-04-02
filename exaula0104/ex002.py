'''
2. Interseção de Conjuntos:
Crie dois conjuntos com seus hobbies e os hobbies de um amigo.
Encontre os hobbies em comum entre vocês e imprima-os
'''

conjunto1 = {'caminhar', 'ler', 'comer', 'estudar'}
conjunto2 = {'jogar', 'ler', 'caminhar', 'nadar', 'fernanda'}
conjunto3 = conjunto1.intersection(conjunto2)

if len(conjunto3) != 0:
    print(f'Seus hobbies em comum são {conjunto3}!')
else:
    print(f'Vocês não tem hobbies em comum!')    
